# Create your tests here.
from django.test import TestCase
from dspace import DSpace
import httplib
__author__ = 'JULIAN'


class TestDSpace(TestCase):

  def test_login_success(self):
      """
      Tests authentication success
      """
      dspace = DSpace("http://45.55.192.223:8443/rest")
      #user created for testing purposes#
      expected_response_code = httplib.OK #200
      response = dspace.login("api_user@example.com","passw0rd_api")
      self.assertTrue(dspace.api_key != "","Login success test fails, API Key not assigned")

  def test_login_fail(self):
      """
      Tests authentication fails
      """
      dspace = DSpace("http://45.55.192.223:8443/rest")
      #user created for testing purposes#
      expected_response_code = httplib.FORBIDDEN #403
      response = dspace.login("api_user@example.com","not_my_password")
      self.assertEqual(expected_response_code,response.status_code, "Login error test fails")

  def test_logout(self):
      """
      Tests Logout
      :return:
      """
      dspace = DSpace("http://45.55.192.223:8443/rest")
      success_response_code = httplib.OK #200
      bad_request_code = httplib.BAD_REQUEST #403
      #login before test log out
      dspace.login("api_user@example.com","passw0rd_api")
      response = dspace.logout()
      self.assertEqual(response.status_code,success_response_code,"Logout test fails")

