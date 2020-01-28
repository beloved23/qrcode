from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.

# APP = (('Android', 'Android'),
#        ('iOS', 'Windows'),
#        ('Mac', 'Mac'),
#        ('Windows', 'Windows'))


class Product(models.Model):
    name = models.CharField(max_length=13, null=True)

    def __str__(self):
        return self.name


class Url(models.Model):
    product = models.ForeignKey(Product, related_name="product_url")
    android = models.CharField(max_length=250, null=True, blank=True)
    ios = models.CharField(max_length=250, null=True, blank=True)
    windows = models.CharField(max_length=250, null=True, blank=True)
    mac = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.product.name

    @property
    def  product_name(self):
        return self.product.name


class Download(models.Model):
    msisdn = models.CharField(max_length=13, null=True)
    status = models.NullBooleanField(default=False)
    device = models.CharField(max_length=50, null=True)
    influencer = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(Product, related_name="product", null=True)

    def __unicode__(self):
        return self.msisdn

    @property
    def app_name(self):
        return self.app.name


# class DownloadUrl():
#     product = models.CharField(max_length=13, null=True)
#     name = models.CharField(choice=APP, max_length=10, null=False)
#     url = models.CharField(max_length=20, null=False)

