from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

# class Company(models.Model):
#   tax_id = models.IntegerField()
#   name = models.CharField(max_length=200)
#   address = models.CharField(max_length=200)
#   email = models.EmailField()
#   phone = models.CharField(max_length=200)


# class Properties(models.Model):
#   beds = models.IntegerField()
#   baths = models.IntegerField()
#   price = models.IntegerField()
#   sqft = models.IntegerField()
#   levels = models.IntegerField()
#   location = models.CharField(max_length=200)
#   date_listed = models.DateField(default=date.today())
#   status = models.CharField(max_length=100)
#   agent = models.ForeignKey(Agents, on_delete=models.CASCADE)

# class Agents(models.Model):
#   license = models.IntegerField()
#   clients = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Users(models.Model):
#   name = models.CharField(max_length=200)
#   address = models.CharField(max_length=200)
#   email = models.EmailField()
#   phone = models.CharField(max_length=200)
#   user_class = models.CharField(max_length=100)
#   password = models.CharField(max_length=100)

# class Client(models.Model):
#   client_pref = models.ForeignKey(Client_pref, on_delete=models.CASCADE)
#   client_fav = models.ManyToManyField(Properties, on_delete=models.CASCADE)

# class Client_pref(models.Model):
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


