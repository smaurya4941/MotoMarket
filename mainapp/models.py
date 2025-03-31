from django.db import models
import uuid
from users.models import Profile,Location
from . consts import CAR_BRANDS,TRANSMISSION
from . utils import user_listing_path
# Create your models here.
class Listing(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(Profile, on_delete=models.CASCADE) #when profile get deleted, all listings will be deleted
    brands=models.CharField(max_length=30,choices=CAR_BRANDS,default=None)
    model=models.CharField(max_length=100)
    plateNumber=models.CharField(max_length=10)
    mileage=models.IntegerField(default=0)
    color=models.CharField(max_length=30,default='white')
    description=models.TextField()
    engine=models.CharField(max_length=30)
    transmission=models.CharField(max_length=30,choices=TRANSMISSION,default=None)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to=user_listing_path)


    def __str__(self) :
        return f'{self.seller.user.username}\'s {self.brands} {self.model}'