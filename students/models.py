from django.db import models

class student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
