from django.db import models
import datetime as dt
# from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


User=settings.AUTH_USER_MODEL
# Create your models here.

class CustomUser(AbstractUser):
    following = models.ManyToManyField(User, blank=True, related_name="followers")

    def save_user(self):
        self.save()

    def follow_user(self,user):
        self.following.add(user)

    def unfollow_user(self, user):
        self.following.remove(user)  

    def get_followers(self):
        return self.followers.all() 

    def get_following(self):
        return self.following.all()           

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_username(cls, username):
        user = CustomUser.objects.get(username__icontains = username)
        profile = cls.objects.get(user = user.id)
        return profile 
    

class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=30, null=True)
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    
    def save_image(self):
        self.save()


    def delete_image(self):
        '''
        Method to delete our images
        '''
        self.delete()    

class Comments(models.Model):
    comment = HTMLField()
    commentor = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    image = models.ForeignKey(Images,related_name='comments', on_delete=models.CASCADE) 

class Like(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)                 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
