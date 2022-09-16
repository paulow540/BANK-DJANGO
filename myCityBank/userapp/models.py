from distutils.command.upload import upload
from enum import unique
from re import U
from django.db import models
from django.contrib.auth.models import User
import random
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class profile(models.Model):

    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("UK", "UK"),
        ("USA", "USA"),
    ]

    states = [
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Osun", "Osun"),
        ("Lagos", "Lagos"),
        ("Kano", "Kano"),
        ("Abuja", "Abuja"),
        
    ]

    position = [
        ("CEO", "CEO"),
        ("GMD", "GMD"),
        ("CTO", "CTO"),
        ("Supervisor", "Supervisor"),
        ("Accountant", "Accountant"),
        ("Marketer", "Marketer"),
        ("Staff", "Staff"),
        ("HR", "HR"),
    ]

    ma_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorce", "Divorce"),
        ("Complicate", "Complicate"),
        
    ]
   
    account = "22" + str(random.randint(000000000, 999999999))


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(unique=False, max_length=20, null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    phone = models.CharField(unique=True, max_length=11, null=True)
    nationality = models.CharField(choices=countries, unique=False, max_length=50, null=True)

    state = models.CharField(choices=states, unique=False, max_length=20, null=True)
    means_of_identity = models.ImageField(upload_to = 'identityImage/', unique=False, null=True)
    particulars =models.FileField(upload_to='particularsImage/', unique=False, null=True)
    profile_passport = models.ImageField(upload_to='staffImage/', unique=False, null=True)
    position = models.CharField(choices=position,unique=False, max_length=20, null=True)
    marital_status = models.CharField(choices=ma_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(default=False, unique=False)
    accont_number = models.CharField(default=account, unique=True, max_length=11)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwarges):
        if created:
            profile.objects.create(user=instance)

    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance,  **kwarges):
        instance.profile.save()