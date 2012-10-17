#encoding:utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('main',
    ('^verify/','verify.views.display'),
)
