# Create your tests here.
from django.test import TestCase
from dspace import DSpace
import httplib
__author__ = 'JULIAN'


class TestDSpace(TestCase):

  def setUp(self):
      self.rest_api_path = "http://45.55.192.223:8443/rest"
      self.dspace = DSpace(self.rest_api_path)
      pass

  def test_login_success(self):
      """
      Tests authentication success
      """
      #user created for testing purposes#
      expected_response_code = httplib.OK #200
      response = self.dspace.login("api_user@example.com","passw0rd_api")
      self.assertTrue(self.dspace.api_key != "","Login success test fails, API Key not assigned")

  def test_login_fail(self):
      """
      Tests authentication fails
      """
      #user created for testing purposes#
      expected_response_code = httplib.FORBIDDEN #403
      response = self.dspace.login("api_user@example.com","not_my_password")
      self.assertEqual(expected_response_code,response.status_code, "Login error test fails")


  def test_logout_previous_login(self):
      """
      Tests  Logout previous login
      """
      success_response_code = httplib.OK #200
      #login before test log out
      self.dspace.login("api_user@example.com","passw0rd_api")
      response = self.dspace.logout()
      self.assertEqual(response.status_code,success_response_code,"Logout test fails")


  def test_logout_no_login(self):
      """
      Tests Logout no previous login
      """
      bad_request_code = httplib.BAD_REQUEST #400
      #login before test log out
      response = self.dspace.logout()
      self.assertEqual(response.status_code,bad_request_code,"Logout test fails")

  



