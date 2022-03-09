from tokenize import Name
from django.test import TestCase

from insta.views import profile
from .models import Profile, Images, CustomUser

from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):

        self.user=CustomUser(username='rue')
        self.user.save()
        self.ruweydha=Profile(user=self.user,bio='I love coding.',profile_photo='default.png')

    def tearDown(self):
        Profile.objects.all().delete()
        CustomUser.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ruweydha, Profile))

    def test_saveProfile(self):
        self.ruweydha.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)

class ImagesTestClass(TestCase):
    def setUp(self):
        self.user=CustomUser(username='aisha')
        self.user.save()
        self.ruweydha=Profile(user=self.user,bio='I love coding.',profile_photo='default.png')
        self.image=Images(id = 1, image='default.png',name='Wildlife',caption='Nature is very beautiful.',profile=self.ruweydha)

    def tearDown(self):
        Images.objects.all().delete()
        Profile.objects.all().delete()
        CustomUser.objects.all().delete()

    def test_insatance(self):
        self.assertTrue(isinstance(self.image, Images))

    def test_save_image(self):
        saved_image=Images.objects.all().delete()
        self.assertTrue((len(saved_image))>0)

    def test_delete_image(self):
        self.image.delete_image()
        deleted_image = Images.objects.all()
        self.assertTrue(len(deleted_image)==0)  
