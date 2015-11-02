"""Conectate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/items/$',views.ItemList.as_view()),
    url(r'^rest/items/(?P<id>[0-9]+)/$',views.ItemDetail.as_view()),
    url(r'^rest/items/search$',views.search_by_keywords),
    url(r'^rest/items/last$',views.get_last_items),
    url(r'^rest/collections/$',views.CollectionList.as_view()),
    url(r'^rest/collections/(?P<id>[0-9]+)/$',views.CollectionDetail.as_view()),
    url(r'^rest/collections/(?P<id>[0-9]+)/items$', views.get_items_by_collection),
    url(r'^rest/communities/$',views.CommunityList.as_view()),
    url(r'^rest/communities/(?P<id>[0-9]+)/$',views.CommunityDetail.as_view()),
    url(r'^rest/communities/top-communities',views.get_top_communities),
    url(r'^rest/communities/(?P<id>[0-9]+)/collections$', views.get_collections_by_community),
    url(r'^rest/bitstreams/$',views.BitstreamList.as_view()),
    url(r'^rest/bitstreams/(?P<id>[0-9]+)/$',views.BitstreamDetail.as_view()),
    url(r'^rest/bitstreams/(?P<id>[0-9]+)/retrieve$',views.get_bitstream_data),
    url(r'^rest/users/$', views.UserList.as_view()),
    url(r'^rest/users/(?P<id>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^rest/groups/$', views.GroupList.as_view()),
    url(r'^rest/groups/(?P<id>[0-9]+)/$', views.GroupDetail.as_view()),
]
