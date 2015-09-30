from django.shortcuts import render
from django.http import Http404
# Create your views here.

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from dspace import Item,DSpace
from Conectate.settings import DSPACE_REST_ENDPOINT

class ItemList(APIView):
    dspace = DSpace(DSPACE_REST_ENDPOINT)
    """
    List all Items, or create a new Item
    """
    def get(self, request,*args,**kwargs):
        items = Item.get_all(self.dspace,**dict(self.request.query_params))
        return Response(items, status=status.HTTP_200_OK)
