# Create your tests here.
from django.test import TestCase
from dspace import DSpace
__author__ = 'JULIAN'


class TestDSpace(TestCase):

  def test_login_success(self):
      """
      Tests authentication success
      """
      dspace = DSpace("http://45.55.192.223:8443/rest")
      #user created for testing purposes#
      expected_response_code = 200
      response = dspace.login("api_user@example.com","passw0rd_api")
      self.assertEqual(expected_response_code,response.status_code, "Login success test fails")

  def test_login_fail(self):
      """
      Tests authentication fails
      """
      dspace = DSpace("http://45.55.192.223:8443/rest")
      #user created for testing purposes#
      expected_response_code = 403
      response = dspace.login("api_user@example.com","not_my_password")
      self.assertEqual(expected_response_code,response.status_code, "Login error test fails")

