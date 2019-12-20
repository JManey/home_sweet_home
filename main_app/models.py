from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
  tax_id = models.IntegerField()
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  is_agent = models.BooleanField(default=False)

# class User_pref(models.Model):
#   user = models.OneToOneField(
#     User,
#     on_delete=models.CASCADE,
#     )
#   beds = models.IntegerField()
#   min_baths = models.IntegerField()
#   max_baths = models.IntegerField()
#   min_price = models.IntegerField()
#   max_price = models.IntegerField()
#   min_sqft = models.IntegerField()
#   max_sqft = models.IntegerField()
#   levels = models.IntegerField()
#   location = models.CharField(max_length=200)
#   school_rating = models.CharField(max_length=100)

# class Property(models.Model):
#   beds = models.IntegerField()
#   baths = models.IntegerField()
#   price = models.IntegerField()
#   sqft = models.IntegerField()
#   levels = models.IntegerField()
#   location = models.CharField(max_length=200)
#   date_listed = models.DateField(default=datetime.now)
#   status = models.CharField(max_length=100)
#   agent = models.ForeignKey(User, on_delete=models.CASCADE)

# class User_fav(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   user_fav = models.ForeignKey(Property, on_delete=models.CASCADE)

