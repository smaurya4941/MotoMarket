#similar to TRiggers in SQL
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile,Location

#creating a profile when a user is created

@receiver(post_save, sender=User)  #when a User object get save on database then run this function given below
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile) #when a Profile object get save on database then run this function given below 
def create_profile_loaction(sender,instance,created,**kwargs):
    if created:
        profile_location=Location.objects.create()
        instance.location=profile_location
        instance.save()
@receiver(post_delete,sender=Profile)
def delete_profile_location(sender,instance,*args,**kwargs):
    if instance.location !=None:
        instance.location.delete()
