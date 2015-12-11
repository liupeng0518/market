# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

protected_loc = settings.PROTECTED_UPLOADS


def download_loc(instance, filename):
    if instance.user.username:
        return "%s/download/%s" % (instance.user.username, filename)
    else:
        return "%s/download/%s" % ("default", filename)
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=500)
    download = models.FileField(upload_to=download_loc, storage=FileSystemStorage(
        location=protected_loc), null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        ordering = ['-order']


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to="products/image/")
    title = models.CharField(max_length=120, null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.title)


class Tag(models.Model):
    product = models.ForeignKey(Product)
    tag = models.CharField(max_length=20)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.tag)


class Category(models.Model):
        # id = models.IntegerField(unichr=True, auto_increment=True, primary_key=True)
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=180)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class CategoryImage(models.Model):
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to="products/image")
    title = models.CharField(max_length=120, null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Category Image'
        verbose_name_plural = 'Category Images'
