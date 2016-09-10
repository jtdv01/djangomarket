from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=50,default="desc")
    item_id = models.IntegerField(default=0)
    price = models.DecimalField(default=0,max_digits=4,decimal_places=2)
    sale_price = models.DecimalField(default=0,max_digits=4,decimal_places=2)
    def __unicode__(self): # def __str___ in py3
        return self.title
