from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    TYPES_USER = [
        ('seller', 'продавец'),
        ('buyer', 'покупатель')
    ]
    buyer = models.CharField(max_length=30, 
    choices = TYPES_USER, 
    default = 'buyer')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


