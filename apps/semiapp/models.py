from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):                                                      # THIS ONE IS OVERSEE THE FORM.
    def basic_validator(self, postData):                                                # BASIC_VALIDATOR MEANS SIMPLE.
        errors = {}                                                                     #
        # check users name                                                              
        if len(postData['first_name']) < 5:                                             # LENGTH TO SEE IF THIS FIELD IS LESS THAN 5
            errors["first_name"] = "User first name should be more than 5 characters"   # IF SO, USER WILL SEE THE ERROR MESSAGE.
        if len(postData['last_name']) < 5:                                              # LENGTH TO SEE IF THIS FIELD IS LESS THAN 5
            errors["last_name"] = "User last name should be more than 5 characters"     # IF SO, USER WILL SEE THE ERROR MESSAGE.
        # check email field for valid email                                             #
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):      # IF EMAIL ADDRESS IS NOT MATCH
            errors['email'] = "invalid email"                                           # LENGTH TO SEE IF THIS FIELD IS LESS THAN 5
        # if email is valid check db for existing email                                 
        else:                                                                           # 
            if len(self.filter(email=postData['email'])) > 1:                           # TO CHECK IF EMAIL ADDRESS HAD BEEN USED.
                errors['email'] = "email already in use"                                # 
        return errors                                                                   # 

class User(models.Model):                                                               # 
    first_name = models.CharField(max_length=255)                                       # 
    last_name = models.CharField(max_length=255)                                        # 
    email = models.CharField(max_length=255)                                            # 
    created_at = models.DateTimeField(auto_now_add=True)                                # 
    updated_at = models.DateTimeField(auto_now=True)                                    # 
    objects = UserManager()                                                             # WHY IS THIS BEING IN THIS CLASS
    def __repr__(self):                                                                 #
        return "User: --{}".format(self.first_name)                                     # RETURN TO THIS CLASS AND POINTER IN THE FIELD OF FIRST NAME