from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    full_name = models.CharField(max_length=254)
    title = models.CharField( max_length=254)
    message = models.TextField(max_length=9000)
    package = models.CharField(max_length=254, null=True)
    date_created = models.DateTimeField( auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=254)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    