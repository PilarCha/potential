
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def validate(self,postData):
        errors=[]
        if len(postData['name'])==0:
            errors.append('Name needs to have something')
        elif not postData['name'].isalpha():
            errors.append('Name can only be letters')
        if len(postData['alias'])==0:
            errors.append('Alias needs to have something')
        if len(postData['email'])==0:
            errors.append('email needs to have something')
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append('Not a valid email')
        if len(postData['pass'])<8:
            errors.append('password needs to have 8 characters')
        if len(postData['confirm'])==0:
            errors.append('confirmation needs to have something')
        if postData['pass']!=postData['confirm']:
            errors.append('Password and Confirm password need to match')
        if postData['birth']==0:
            errors.append('Please put something in the birthdayfield!')
        return errors
    def login(self,postData):
        errors=[]
        if len(postData['lemail'])==0:
            errors.append('Login email needs to have something')
        elif not EMAIL_REGEX.match(postData['lemail']):
            errors.append('Not a valid login email')
        if len(postData['lpass'])==0:
            errors.append('login password needs to have something in it')
        return errors


class User(models.Model):
    name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    birth=models.CharField(max_length=255)
    updated_at=models.DateTimeField(auto_now = True)
    objects=UserManager()
class FriendShip(models.Model):
    creator=models.ForeignKey(User,related_name='friendo')
    friend=models.ForeignKey(User,related_name='who')



# Create your models here.
