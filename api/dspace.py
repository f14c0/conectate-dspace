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




