from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    seller = models.BooleanField()
    buyer = models.BooleanField()
    
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    seller = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


