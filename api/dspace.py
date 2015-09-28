__author__ = 'JULIAN'
import requests
import httplib

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
    def __init__(self, **kwargs):
        ##TODO Item instantiation
        return

    def get_all(self,**kwargs):
        """
        Returns an array of items, gathered from DSpace REST API
        :param kwargs: filters
        :return:
        """
        #TODO get all items
        return None

    def get_item(self, id,**kwargs):
        """
        Retrieve an Item by Id
        :param id: item id
        :param kwargs: item expand options
        :return:
        """
        #TODO get item by Id
        return None

    def get_item_metadata(self,item_id):
        """
        Returns item metadata as a dictionary
        :param item_id:
        :return:
        """
        #TODO return metadata form item
        return None

