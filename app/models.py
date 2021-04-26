"""
Definition of models.
"""

from django.db import models

# Create your models here.

class RegistrantInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True)
    notsick = models.BooleanField(default=False, verbose_name="Not feeling any symptoms")

    def __str__(self):
        return self.first_name + self.last_name

