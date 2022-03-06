from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

    def save_profile(self):
        self.save()

class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    
    def save_image(self):
        self.save()


