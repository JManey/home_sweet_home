from django.db import models
from django.urls import reverse
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
  def __str__(self):
    return f"{self.is_agent}"
  def get_absolute_url(self):
      return reverse("agent_detail", kwargs={"agent_id": self.id})

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

class Property(models.Model):
  street_address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  beds = models.IntegerField()
  baths = models.FloatField()
  price = models.IntegerField()
  sqft = models.IntegerField()
  levels = models.IntegerField()
  date_listed = models.DateField(default=datetime.now)
  status = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.street_address}"

  def get_absolute_url(self):
      return reverse("detail", kwargs={"property_id": self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  property = models.ForeignKey(Property, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for property_id: {self.property.id} @{self.url}"

# class User_fav(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   user_fav = models.ForeignKey(Property, on_delete=models.CASCADE)

