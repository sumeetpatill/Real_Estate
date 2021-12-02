from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.DecimalField(decimal_places=1,max_digits=2)
    bathrooms = models.DecimalField(decimal_places=1,max_digits=2)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)

def _str_(self):
    return self.title