from typing import Any

from django.contrib.auth.models import User
from django.db import models

# my  models .

class Personal(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    def __str__(self):
        return self.details
