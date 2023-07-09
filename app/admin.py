from django.contrib import admin
from .models import TestRide, Bike, Color, ContactUs, Category
# Register your models here.

admin.site.register(TestRide)
admin.site.register(Bike)
admin.site.register(Color)
admin.site.register(ContactUs)
admin.site.register(Category)