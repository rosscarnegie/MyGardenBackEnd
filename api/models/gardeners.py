from django.db import models
from django.utils import timezone

# The tool below makes this project translatable. 
# Doing so requires hooks called translation strings and tell Django 
# that the text should be translated into the end user's language.
from django.utils.translation import gettext_lazy as gtl

# The AbstractBaseUser tells django that I'm making a custom user model.
from django.contrib.auth.models import AbstractBaseUser 

# Lets me use django's permission framework into my user class. 
from django.contrib.auth.models import PermissionsMixin

#
from django.contrib.auth.models import BaseUserManager


class GardenerManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
            'Superuser must be assigned to is_staff=True'
            )
        return self.create_user(email, user_name, password, **other_fields)


    def create_user(self, email, user_name, password=None, **other_fields):

        if not email:
            raise ValueError(gtl('You must provide an email address'))
        if not user_name:
            raise ValueError(gtl('You must provide a unique username'))

        user = self.model(email=self.normalize_email(email), user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Gardener(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gtl('email address'), unique=True)
    user_name = models.CharField(gtl('username'), max_length=20, unique=True)
    zipcode = models.CharField(gtl('zipcode'), max_length=5, blank=True)
    zone = models.CharField(gtl('Your USDA Hardiness Zone'), max_length=3, blank=True, null=True)
    about = models.CharField(gtl('About me'), max_length=300, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')

    objects = GardenerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

# This tells Django that when we create a superuser, they also need to provide
# a username. 
    #REQUIRED_FIELDS = ['user_name',]

    def __str__(self):
        return self.email 