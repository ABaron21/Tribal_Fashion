from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    town_or_city = models.CharField(max_length=254, null=True, blank=True)
    county = models.CharField(max_length=254, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=False)
    retailer_requested = models.BooleanField(default=False)
    retailer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class RetailAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, default='', blank=False)
    last_name = models.CharField(max_length=50, null=False, default='', blank=False)
    subscribed = models.BooleanField(null=False, default=False, blank=False)
    cancel_subscription = models.BooleanField(null=False, default=False, blank=False)

    def __str__(self):
        return self.user.username
