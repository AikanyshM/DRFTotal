from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    seller = models.BooleanField(default=True)
    TYPES_USER = [
        ('seller', 'продавец'),
        ('buyer', 'покупатель')
    ]
    buyer = models.CharField(max_length=30, 
    choices = TYPES_USER, 
    default = 'buyer')
    def __str__(self):
        return self.username

