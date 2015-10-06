# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Community(models.Model):
	name = models.CharField(max_length=100)
	handle = models.CharField(max_length=500)
	type= models.CharField(max_length=30)
	link = models.CharField(max_length=500)
	parentCommunity = models.ForeignKey("self")
	license=models.CharField(max_length=30)
	copyrightText= models.CharField(max_length=500)
	introductoryText =models.CharField(max_length=500)

class Collection(models.Model):
	name = models.CharField(max_length=100)
	handle = models.CharField(max_length=500)
	type= models.CharField(max_length=30)
	link = models.CharField(max_length=500)
	parentCommunity = models.ForeignKey(Community)
	license=models.CharField(max_length=30)
	copyrightText= models.CharField(max_length=500)
	introductoryText =models.CharField(max_length=500)
	shortDescription=models.CharField(max_length=500)

class Item (models.Model):
	name = models.CharField(max_length=100)
	handle = models.CharField(max_length=500)
	type= models.CharField(max_length=30)
	link = models.CharField(max_length=500)
	parentCollection = models.ForeignKey(Collection)
	