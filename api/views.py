from django.shortcuts import render
from django.http import Http404

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from dspace import Item,DSpace,Collection,Community,Bitstream
from Conectate.settings import DSPACE_REST_ENDPOINT


from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from api.serializers import UserSerializer


import json

dspace = DSpace(DSPACE_REST_ENDPOINT)

#fuction based views

@api_view(['GET'])
def get_items_by_collection(request,id):
    """
    Return all items of the specified collection.
    """
    try:
        items =  Collection.get_items(dspace,id,**dict(request.query_params))
        return  Response(items, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        raise Http404

@api_view(['GET'])
def get_bitstream_data(request,id):
    """
    Return data from an especified bitstream.
    """
    try:
        bitstream_data =  Bitstream.retrieve(dspace,id,**dict(request.query_params))
        response = Response(status=status.HTTP_200_OK)
        response.content = bitstream_data
        return  response
    except Collection.DoesNotExist:
        raise Http404

@api_view(['GET'])
def search_by_keywords(request):
    """
    Returns an array of items, which match with given keywords
    """
    keywords = request.query_params['q'].split()
    items = Item.search_by_keywords(dspace,keywords)
    return Response(items,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_top_communities(request):
    """
    Return  top level communities array
    """
    communities = Community.get_top_communities(dspace,**dict(request.query_params))
    return Response(communities,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_collections_by_community(request,id):
    """
    Return all collections of the specified community.
    """
    try:
        collections =  Community.get_collections(dspace,id,**dict(request.query_params))
        return  Response(collections, status=status.HTTP_200_OK)
    except Community.DoesNotExist:
        raise Http404

@api_view(['GET'])
def get_last_items(request):
    """
    Return an array of items, sorted desc by date modified
    """
    items = Item.get_lastest(dspace,**dict(request.query_params))
    return  Response(items, status=status.HTTP_200_OK)


#class based views
#TODO Refactor

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

class CollectionList(APIView):
    """
    List all collections or create a new Collection
    """
    def get(self,request,*args,**kwargs):
        collections = Collection.get_all(dspace,**dict(self.request.query_params))
        return Response(collections, status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        #TODO
        pass

class CollectionDetail(APIView):
    """
    Retrieve, update or delete Collection instance
    """
    def get_object(self,id,**kwargs):
        try:
            collection = Collection.get_collection(dspace,id,**dict(kwargs))
            return collection
        except Collection.DoesNotExist:
            raise Http404

    def get(self,request,id, *args,**kwargs):
        collection = self.get_object(id,**dict(self.request.query_params))
        collection_response = json.JSONDecoder().decode(json.dumps(collection.__dict__))
        return Response(collection_response)

    def put(self,request,id, *args,**kwargs):
        #TODO
        pass

    def delete(self,request,id, *args,**kwargs):
        #TODO
        pass

class CommunityList(APIView):
    """
    List all communities or create a new Community
    """
    def get(self,request,*args,**kwargs):
        communities = Community.get_all(dspace,**dict(self.request.query_params))
        return Response(communities, status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        #TODO
        pass

class CommunityDetail(APIView):
    """
    Retrieve, update or delete Community instance
    """
    def get_object(self,id,**kwargs):
        try:
            community = Community.get_community(dspace,id,**dict(kwargs))
            return community
        except Community.DoesNotExist:
            raise Http404

    def get(self,request,id, *args,**kwargs):
        community = self.get_object(id,**dict(self.request.query_params))
        community_response = json.JSONDecoder().decode(json.dumps(community.__dict__))
        return Response(community_response)

    def put(self,request,id, *args,**kwargs):
        #TODO
        pass

    def delete(self,request,id, *args,**kwargs):
        #TODO
        pass

class BitstreamList(APIView):
    """
    List all bitstreams or create a new Bitstream
    """
    def get(self,request,*args,**kwargs):
        bitstreams = Bitstream.get_all(dspace,**dict(self.request.query_params))
        return Response(bitstreams, status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        #TODO
        pass

class BitstreamDetail(APIView):
    """
    Retrieve, update or delete Bitstream instance
    """
    def get_object(self,id,**kwargs):
        try:
            bitstream = Bitstream.get_bitstream(dspace,id,**dict(kwargs))
            return bitstream
        except Bitstream.DoesNotExist:
            raise Http404

    def get(self,request,id, *args,**kwargs):
        bitstream = self.get_object(id,**dict(self.request.query_params))
        bitstream_response = json.JSONDecoder().decode(json.dumps(bitstream.__dict__))
        return Response(bitstream_response)

    def put(self,request,id, *args,**kwargs):
        #TODO
        pass

    def delete(self,request,id, *args,**kwargs):
        #TODO
        pass

        bitstream

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        user = UserSerializer(user)
        return Response(user.data)

    @csrf_exempt
    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
