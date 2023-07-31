from django.db import models
import random

# Create your models here.
class Certificate(models.Model):
    # certificate_id = models.IntegerField(random.randint)
    name = models.CharField(max_length=100)
    date = models.DateField('%d-%m-%Y')
    sign = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

