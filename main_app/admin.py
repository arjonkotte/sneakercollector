from django.contrib import admin

# Register your models here.
from .models import Sneaker, Cleaning
admin.site.register(Sneaker)
admin.site.register(Cleaning)


