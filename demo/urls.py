#encoding:utf-8
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^main/',include('main.urls')),
)
