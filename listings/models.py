from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from listings.choices import status_choices, type_home_choices, state_choices


class Listing(models.Model):
    HOME_STATUS = [(key, value) for key, value in status_choices.items()]
    HOME_TYPE = [(key, value) for key, value in type_home_choices.items()]
    ALL_STATES = [(key, value) for key, value in state_choices.items()]

    objects = models.Manager()
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=ALL_STATES)
    zipcode = models.CharField(max_length=20)
    type_of_home = models.CharField(max_length=30, choices=HOME_TYPE)
    status = models.CharField(max_length=20, choices=HOME_STATUS)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
