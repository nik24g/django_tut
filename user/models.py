import email
from django.db import models

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