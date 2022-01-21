from datetime import date
from distutils.command.upload import upload
import email
from email.headerregistry import Address
from statistics import mode
from unicodedata import category
from django.db import models
from .managers import CustomUserManager

from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    # problem = models.TextField()
    problem = models.CharField(max_length=700)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    pass

class User(AbstractUser):
    username = None
    # Id = models.AutoField
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, default="")
    address = models.TextField(default="")
    # date = models.DateField()
    image = models.ImageField(upload_to='user/image', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=100)
    dsc = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user/product', null=True, blank=True)

    def __str__(self):
        return self.name