from django.contrib import admin
from .models import Hostel, Tenant
# Register your models here.

admin.site.register([Hostel, Tenant])