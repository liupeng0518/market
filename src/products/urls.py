# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url

<<<<<<< HEAD
=======

>>>>>>> develop
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('products.views',
                       url(r'^$', 'list_all', name="all_products"),

                       url(r'^add/',
                           'add_product', name="add_product"),

                       url(r'^(?P<slug>.*)/edit/',
                           'edit_product', name="edit_product"),


                       url(r'^(?P<slug>.*)/images/',
                           'manage_product_image', name="manage_product_image"),

                       url(r'^(?P<slug>.*)/$', 'single',
                           name="single_product"),

                       )
