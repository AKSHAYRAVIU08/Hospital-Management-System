from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Sign(AbstractUser):
    pass


class Submit(models.Model):
    patient_name=models.CharField(max_length=40, null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    gender=models.CharField(max_length=20, null=True, blank=True)
    place=models.CharField(max_length=40, null=True, blank=True)
    disease=models.CharField(max_length=30, null=True, blank=True)


