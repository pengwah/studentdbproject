from django.db import models
import datetime

class student(models.Model):
    firstname = models.CharField(max_length=40)
    middlename = models.CharField(max_length=40, null=True)
    lastname = models.CharField(max_length=40)
    birthdate = models.DateField(null=True)
    email = models.EmailField(null=True)
