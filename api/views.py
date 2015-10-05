from django.shortcuts import render
from django.http import Http404

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from dspace import Item,DSpace
from Conectate.settings import DSPACE_REST_ENDPOINT

import json


dspace = DSpace(DSPACE_REST_ENDPOINT)

class ItemList(APIView):
    """
    List all Items, or create a new Item
    """
    dspace = DSpace(DSPACE_REST_ENDPOINT)
    def get(self, request,*args,**kwargs):
        items = Item.get_all(self.dspace,**dict(self.request.query_params))
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request , *args, **kwargs):
        #TODO
        pass

class ItemDetail(APIView):
    """
    Retrieve, update or delete Item instance
    """
    dspace = DSpace(DSPACE_REST_ENDPOINT)
    #TODO fix link property in Item object
    def get_object(self, id,**kwargs):
        try:
            item = Item.get_item(dspace,id,**dict(kwargs))
            return item
        except Item.DoesNotExist:
            raise Http404

    def get(self,request,id,*args,**kwargs):
        item = self.get_object(id,**dict(self.request.query_params))
        item_response = json.JSONDecoder().decode(json.dumps(item.__dict__))
        return Response(item_response)

    def put(self, request, id,*args,**kwargs):
        #TODO
        pass
    def delete(self,request,id,*args,**kwargs):
        #TODO
        pass
