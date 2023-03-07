from django.contrib import admin
from .models import UserAccount, RetailAccount

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(RetailAccount)
