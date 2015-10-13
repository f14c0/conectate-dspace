# Create your tests here.
import httplib

from django.test import TestCase

from dspace import DSpace,Item,Community,Collection
from django.core.exceptions import ObjectDoesNotExist

__author__ = 'JULIAN'


class TestDSpace(TestCase):
  #TODO Refactor in new Item tests in new TestCase

  def setUp(self):
      self.rest_api_path = "http://45.55.192.223:8443/rest"
      #self.rest_api_path = "https://trydspace.longsight.com/rest"
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

  #ITEM Class Test
  #TODO Refactor

  def test_get_all_items(self):
      """
      Test Retrieving all items
      """
      dspace= self.dspace
      items = Item.get_all(dspace)
      self.assertGreater(len(items),0)

  def test_get_all_items_with_limit(self):
      """
      Test Retrieving all items with limit
      """
      dspace= self.dspace
      max_items = 5
      items = Item.get_all(dspace,limit=[max_items])
      self.assertLessEqual(len(items),max_items)

  def test_get_item(self):
      """
      Test Retrieving an item by Id
      """
      dspace = self.dspace
      test_id = 5
      item = Item.get_item(dspace,test_id)
      self.assertEqual(item.id,test_id,"Get item by Id Fails")

  def test_get_item_with_metadata(self):
      """
      Test Retrieving an item by Id
      """
      dspace= self.dspace
      test_id = 5
      item = Item.get_item(dspace,test_id,expand=["metadata"])
      self.assertIsNotNone(item.metadata,"Item metadata not retrieved")

  def test_get_item_metadata(self):
      """
      Test Retrieving an item by Id
      """
      dspace= self.dspace
      test_id = 5
      metadata = Item.get_item_metadata(dspace,test_id)
      self.assertGreater(len(metadata),0)

  def test_find_by_metadata_field(self):
      """
      Test searching items by metadata field
      """
      #test using known item and field
      #TODO test with dynamic items and metadata fields
      dspace = self.dspace
      language ="en_US"
      field = "lom.general.keyword"
      value = "anatomia"
      items = Item.find_by_metadata_field(dspace,field,value,language)
      self.assertIsNotNone(items)
      self.assertGreater(len(items),0)

  def test_search_by_keywords(self):
      """
      Test searching by keywords
      """
      dspace = self.dspace
      keywords = ["anatomia","prueba"]
      items = Item.search_by_keywords(dspace,keywords)
      self.assertIsNotNone(items)
      self.assertGreaterEqual(len(items),2)

  #Collection Class Test
  #TODO Refactor

  def test_get_all_collections(self):
      """
      Test Retrieving all collections
      """
      dspace= self.dspace
      collections = Collection.get_all(dspace)
      self.assertGreater(len(collections),0)

  def test_get_all_collections_with_limit(self):
      """
      Test Retrieving all collections with limit
      """
      dspace= self.dspace
      max_collections = 5
      collections = Collection.get_all(dspace,limit=[max_collections])
      self.assertLessEqual(len(collections),max_collections)

  def test_get_community(self):
      """
      Test Retrieving an collection by Id
      """
      dspace= self.dspace
      test_id = 2
      collection = Collection.get_collection(dspace,test_id)
      self.assertEqual(collection.id,test_id,"Get collection by Id Fails")

  def test_get_collection_items(self):
      """
      Test retrieving all items from an especific collection
      """
      dspace =  self.dspace
      test_id = 2
      items = Collection.get_items(dspace,test_id,expand=["parentCollection"])
      self.assertIsNotNone(items)
      self.assertRaises
      for item in items:
          item_temp = Item(dict(item))
          self.assertEqual(test_id,item_temp.parentCollection["id"])

  def test_get_not_found_collection_items(self):
      """
      Test retrieving all items from an especific not found collection
      """
      dspace =  self.dspace
      test_id = -1
      self.assertRaises(Collection.DoesNotExist,lambda:Collection.get_items(dspace,test_id,expand=["parentCollection"]))

  #Comunity Class Test
  #TODO Refactor

  def test_get_all_communities(self):
      """
      Test Retrieving all communities
      """
      dspace= self.dspace
      communities = Community.get_all(dspace)
      self.assertGreater(len(communities),0)

  def test_get_all_communities_with_limit(self):
      """
      Test Retrieving all communities with limit
      """
      dspace= self.dspace
      max_communities = 5
      communities = Community.get_all(dspace,limit=[max_communities])
      self.assertLessEqual(len(communities),max_communities)

  def test_get_community(self):
      """
      Test Retrieving an community by Id
      """
      dspace= self.dspace
      test_id = 2
      community = Community.get_community(dspace,test_id)
      self.assertEqual(community.id,test_id,"Get community by Id Fails")

  def test_get_top_communities(self):
      """
      Test retrieving top level communities
      """
      dspace = self.dspace
      communities = Community.get_top_communities(dspace,expand=["parentCommunity"])
      self.assertIsNotNone(communities)
      for com in communities:
          self.assertIsNone(com['parentCommunity'])
