from django.contrib import admin
from .models import News, Car, Pet, Phone, Home
# Register your models here.


admin.site.register(Car)
admin.site.register(News)
admin.site.register(Pet)
admin.site.register(Phone)
admin.site.register(Home)
