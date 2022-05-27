from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    full_name = models.CharField(max_length=254)
    title = models.CharField( max_length=254)
    message = models.TextField(max_length=9000)
    package = models.CharField(max_length=254, null=True)
