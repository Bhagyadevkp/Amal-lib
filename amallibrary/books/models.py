import datetime
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    booknumber = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



class takenbooks(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    renewalstatus = models.BooleanField(default=False)
    renewaldate = models.DateTimeField(default=timezone.now)
    returnstatus = models.BooleanField(default=False)
    returndate = models.DateTimeField(default=timezone.now)

    def int(self):
        return self.book


class booktakingdatabase(models.Model):
    booknumber = models.IntegerField()
    username = models.CharField(max_length=100)
    takendate = models.DateTimeField(default=timezone.now)
    returndate = models.DateTimeField(default=timezone.now)

    def int(self):
        return self.book

