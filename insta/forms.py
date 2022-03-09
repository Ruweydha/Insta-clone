from pyexpat import model
from django import forms
from .models import Profile, Images, Comments

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date']    

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['profile', 'date_posted']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude =['commentor', 'date_posted', 'image' ]