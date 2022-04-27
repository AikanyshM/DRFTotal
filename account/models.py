from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    seller = models.BooleanField(default=True)
    buyer = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.username

