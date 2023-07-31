# models.py

from django.db import models

class Certificate(models.Model):
    c_id = models.CharField(max_length=100, unique=True)
    # Add other fields if necessary

