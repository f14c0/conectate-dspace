__author__ = 'JULIAN'
import requests
import httplib
import json
from django.core.exceptions import ObjectDoesNotExist

class DSpace:
    """
    Class DSpace provide methods for interacting with  DSpace REST API
    """
    def __init__(self,rest_path):
        """
        :param rest_path: URL for DSpace API endpoint
        :return:
        """
        self.rest_path = rest_path
        self.api_key = ""

    def login(self,user, password):
        """
        Makes a request to rest API in order to authenticate an user
        :param user:user email
        :param password: user password
        :return: http response
        """
        #request setup
        payload = '{"email":"'+user  +'", "password":"'+password+'"}'
        headers = {'Content-Type':'application/json'}
        url = self.rest_path + "/login"
        response = requests.post(url,data= payload ,headers = headers)
        #200
        if response.status_code == httplib.OK:
            self.api_key = response.text
        return response

    def logout(self):
        """
        Makes a request to rest API in order to logout an user
        :return: http response
        """
        #request setup
        headers = {'Content-Type':'application/json' , 'rest-dspace-token': self.api_key }
        url =  self .rest_path + "/logout"
        response =  requests.post(url,headers = headers )
        return response

class Item :
    DoesNotExist = ObjectDoesNotExist
    """
    Class Item provide methods for interacting with Items from  DSpace REST API
    """
    #TODO code refactor of kwargs to query paramas piece of code
    def __init__(self, dict ,**kwargs):
        self.__dict__ = dict

    @staticmethod
    def get_all(dspace,**kwargs):
        """
        Returns an array of items, gathered from DSpace REST API
        :param kwargs: filters
        :return:
        """
        #convert kwargs in query params

        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/items" + query_params
        print url
        response = requests.get(url,headers=headers)
        items =  json.loads(response.text)
        return items

    @staticmethod
    def get_item(dspace, item_id,**kwargs):
        """
        Retrieve an Item by Id
        :param id: item id
        :param kwargs: item expand options
        :return: Item
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))

        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/items/" + str(item_id) + query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            item =  Item(json.loads(response.text))
        elif response.status_code == httplib.NOT_FOUND:
            raise Item.DoesNotExist
        return item

    @staticmethod
    def get_item_metadata(dspace,item_id,**kwargs):
        """
        Returns item metadata as a dictionary
        :param item_id:
        :return:
        """
        #request setup

        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/items/" + str(item_id) + "/metadata" +query_params
        print url
        response = requests.get(url,headers=headers)
        metadata = None
        if response.status_code == httplib.OK:
            metadata =  json.loads(response.text)
        return metadata

    def save(self,**kwargs):
        """
        :param kwargs:
        :return: returns the item saved
        """
        #TODO
        pass

    def delete(self,**kwargs):
        #TODO
        pass

    @staticmethod
    def find_by_metadata_field(dspace,key,value,language,**kwargs):
        #request setup
        payload = '{{"key":"{0}","value": "{1}","language": "{2}"}}'.format(str(key),str(value),str(language))
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/items/find-by-metadata-field"
        print url
        response = requests.post(url,data= payload ,headers = headers)
        if response.status_code == httplib.OK:
            items =  json.loads(response.text)
        return items

    @staticmethod
    def search_by_keywords(dspace,keywords,**kwargs):
        """
        Returns an array of items, gathered from DSpace REST API,
        which match with given keywords
        :param kwargs: filters
        :return: Item array
        """
        items_response=[]
        items_dict={}
        if keywords is not None:
            for kw in keywords:
                if len(kw) <= 2:
                    continue
                else:
                    #improve mechanism to set up language an metadata field
                    #TODO
                    language ="en_US"
                    field = "lom.general.keyword"
                    items = Item.find_by_metadata_field(dspace,field,kw,language)

                    if items is not None:
                        for item in items:
                            items_dict[item['id']]=item
                    else:
                        return items_response
            #parse dict to items_response
            for value in items_dict.itervalues():
                items_response.append(value)
        return items_response


class Collection :
    DoesNotExist = ObjectDoesNotExist
    """
    Class Collection provide methods for interacting with Collections from  DSpace REST API
    """
    def __init__(self,dict,**kwargs):
        self.__dict__ = dict

    @staticmethod
    def get_all(dspace,**kwargs):
        """
        Returns an array of collections, gathered from DSpace REST API
        :param kwargs: filters
        :return:
        """
        #convert kwargs in query params

        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/collections" + query_params
        response = requests.get(url,headers=headers)
        collections =  json.loads(response.text)
        return collections

    @staticmethod
    def get_collection(dspace, collection_id,**kwargs):
        """
        Retrieve an Collection by Id
        :param collection_id: collection id
        :param kwargs: Collection expand options
        :return: Collection
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))

        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/collections/" + str(collection_id) + query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            collection =  Collection(json.loads(response.text))
        elif response.status_code == httplib.NOT_FOUND:
            raise Collection.DoesNotExist
        return collection

    @staticmethod
    def get_items(dspace,collection_id,*args,**kwargs):
        """
        Retrieve items in a especific collection
        :param collection_id: collection id
        :param kwargs: Collection expand options
        :return: Item array
        """
        #convert kwargs in query params

        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/collections/"+str(collection_id)+"/items"+ query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            items =  json.loads(response.text)
        elif response.status_code == httplib.NOT_FOUND:
            raise Collection.DoesNotExist

        return items

    def save(self,**kwargs):
        #TODO
        pass
    def delete(self,**kwargs):
        #TODO
        pass

class Community:
    DoesNotExist = ObjectDoesNotExist
    """
    Class Community provide methods for interacting with Communities from  DSpace REST API
    """
    #TODO code refactor of kwargs to query paramas piece of code

    def __init__(self, dict ,**kwargs):
        self.__dict__ = dict

    @staticmethod
    def get_all(dspace,**kwargs):
        """
        Returns an array of communities, gathered from DSpace REST API
        :param kwargs: filters
        :return: communities array
        """
        #convert kwargs in query params

        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/communities" + query_params
        print url
        response = requests.get(url,headers=headers)
        communities =  json.loads(response.text)
        return communities


    @staticmethod
    def get_community(dspace, item_id,**kwargs):
        """
        Retrieve an Community by Id
        :param id: community id
        :param kwargs: community expand options
        :return: Community
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))

        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/communities/" + str(item_id) + query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            community =  Community(json.loads(response.text))
        elif response.status_code == httplib.NOT_FOUND:
            raise Community.DoesNotExist
        return community

class Bitstream :
    DoesNotExist = ObjectDoesNotExist
    """
    Class Bitstream provide methods for interacting with Bitstreams from  DSpace REST API
    """
    #TODO code refactor of kwargs to query paramas piece of code
    def __init__(self, dict ,**kwargs):
        self.__dict__ = dict

    @staticmethod
    def get_all(dspace,**kwargs):
        """
        Returns an array of bitstream, gathered from DSpace REST API
        :param kwargs: filters
        :return:
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/bitstreams" + query_params
        print url
        response = requests.get(url,headers=headers)
        bitstreams =  json.loads(response.text)
        return bitstreams

    @staticmethod
    def get_bitstream(dspace, bitstream_id,**kwargs):
        """
        Retrieve an Bitstream by Id
        :param id: bitstream id
        :param kwargs: bitstream expand options
        :return: Bitstream
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))

        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/bitstreams/" + str(bitstream_id) + query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            bitstream =  Bitstream(json.loads(response.text))
        elif response.status_code == httplib.NOT_FOUND:
            raise Bitstream.DoesNotExist
        return bitstream

    @staticmethod
    def retrieve(dspace,bitstream_id,**kwargs):
        """
        Retrieve bitstream data gathered from DSpace REST API
        :param id: bitstream id
        :param kwargs: bitstream options
        :return:
        """
        #convert kwargs in query params
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))

        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/bitstreams/" +str(bitstream_id)+"/retrieve"+query_params
        print url
        response = requests.get(url,headers=headers)

        if response.status_code == httplib.OK:
            data =  response.content
        elif response.status_code == httplib.NOT_FOUND:
            raise Bitstream.DoesNotExist
        return data
