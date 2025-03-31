from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path
# from localflavor.us.models import USStateField

# Create your models here.
class Location(models.Model):
    address_1=models.CharField(max_length=150)
    address_2=models.CharField(max_length=150,blank=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100 ,default='UP')
    zip_code=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'Location {self.id}'
    


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) #models.cascade means when user is deleted then profile is also deleted
    photo=models.ImageField(null=True,upload_to=user_directory_path)
    bio=models.CharField(max_length=200, blank=True)
    phone_number=models.CharField(max_length=12, blank=True)
    location=models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return f'{self.user.username}\'s Profile '

