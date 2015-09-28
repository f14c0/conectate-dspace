from django.shortcuts import render
from django.contrib.auth.models import User
from models import *
from django.http import Http404

from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
	"""
	List all users, or create a new user.
	"""
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
	"""
	Retrieve, update or delete a user instance.
	"""
	def get_object(self, pk):
		try:
		    return User.objects.get(pk=pk)
		except User.DoesNotExist:
		    raise Http404

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		user = UserSerializer(user)
		return Response(user.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class CommunityList(APIView):
	"""
	List all Communities, or create a new Community.
	"""
	def get(self, request, format=None):
		communities = Community.objects.all()
		serializer = CommunitySerializer(communities, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CommunitySerializer(data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		community = self.get_object(pk)
		community.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CommunityDetail(APIView):
	"""
	Retrieve, update or delete a Community instance.
	"""
	def get_object(self, pk):
		try:
		    return Community.objects.get(pk=pk)
		except Community.DoesNotExist:
		    raise Http404

	def get(self, request, pk, format=None):
		community = self.get_object(pk)
		community = CommunitySerializer(community)
		return Response(community.data)

	def put(self, request, pk, format=None):
		community = self.get_object(pk)
		serializer = CommunitySerializer(community, data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		community = self.get_object(pk)
		community.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)








class CollectionList(APIView):
	"""
	List all Collection, or create a new Collection.
	"""
	def get(self, request, format=None):
		collections = Collection.objects.all()
		serializer = CollectionSerializer(collections, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CollectionSerializer(data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		collection = self.get_object(pk)
		collection.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionDetail(APIView):
	"""
	Retrieve, update or delete a Collection instance.
	"""
	def get_object(self, pk):
		try:
		    return Collection.objects.get(pk=pk)
		except Collection.DoesNotExist:
		    raise Http404

	def get(self, request, pk, format=None):
		community = self.get_object(pk)
		community = CollectionSerializer(community)
		return Response(community.data)

	def put(self, request, pk, format=None):
		community = self.get_object(pk)
		serializer = CollectionSerializer(community, data=request.DATA)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		community = self.get_object(pk)
		community.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



