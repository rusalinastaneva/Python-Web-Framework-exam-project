from datetime import datetime

from django.db import models


# Create your models here.
class TeamMembers(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
