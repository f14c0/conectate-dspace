from django.contrib.auth.models import User
from models import *

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
	fields = ('id', 'username', 'first_name', 'last_name', 'email')

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection


