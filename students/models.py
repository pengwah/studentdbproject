from django.db import models
import datetime

class student(models.Model):
    firstname = models.CharField(max_length=40)
    middlename = models.CharField(max_length=40, null=True, blank=True)
    lastname = models.CharField(max_length=40)
    fullname = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True)
    email2 = models.EmailField(null=True)
    phone1 = models.CharField(max_length=12, null=True)
    phone2 = models.CharField(max_length=12, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    zipcode = models.CharField(max_length=12, null=True, blank=True)
    inactive = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['fullname'], name='fullname_idx'),
        ]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id)])

class instrument(models.Model):
    instrument = models.CharField(max_length=30, null=True, blank=True)

class instructor(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)

class studentinstrument(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE, null=True)
    instrument = models.ForeignKey(instrument, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(instructor, on_delete=models.CASCADE, null=True)
