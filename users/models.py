from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    image = models.ImageField(default="default.png", upload_to = "profile_pics", editable = True, blank=True)
    phone_number = models.CharField(max_length=16)
    address = models.TextField(max_length=355)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"


