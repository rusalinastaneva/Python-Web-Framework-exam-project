from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from listings.choices import STATE_CHOICES, STATUS_CHOICES, TYPE_HOME_CHOICES, BEDROOM_CHOICES
from listings.validators import validate_price_is_negative_or_zero, city_start_with_uppercase_letter, \
    us_zipcode_consists_of_five_digits, validate_bedrooms_is_negative_or_zero, validate_bathrooms_is_negative_or_zero, \
    validate_garage_is_negative, validate_sqft_is_negative_or_zero, validate_lot_size_is_negative_or_zero


class Listing(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100, validators=(city_start_with_uppercase_letter,))
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=20, validators=(us_zipcode_consists_of_five_digits,))
    type_of_home = models.CharField(max_length=30, choices=TYPE_HOME_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(blank=True)
    price = models.IntegerField(validators=(validate_price_is_negative_or_zero,))
    bedrooms = models.IntegerField(choices=BEDROOM_CHOICES, validators=(validate_bedrooms_is_negative_or_zero,))
    bathrooms = models.IntegerField(validators=(validate_bathrooms_is_negative_or_zero,))
    garage = models.IntegerField(validators=(validate_garage_is_negative,))
    sqft = models.IntegerField(validators=(validate_sqft_is_negative_or_zero,))
    lot_size = models.DecimalField(
        "Lot size (Acres)",
        max_digits=5,
        decimal_places=1,
        validators=(validate_lot_size_is_negative_or_zero,)
    )
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=False)

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
