__author__ = 'JULIAN'
import requests
import httplib
import json

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
        print (kwargs)
        query_params="?"
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                query_params += "{0}={1}&".format(str(key),str(value[0]))
        #request setup
        headers = {'Content-Type':'application/json'}
        url = dspace.rest_path + "/items" + query_params
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
        item = None
        if response.status_code == httplib.OK:
            item =  Item(json.loads(response.text))
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

