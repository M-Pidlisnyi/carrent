from django.contrib import admin
from .models import BodyStyle, Car, CarInstance, Brand

# Register your models here.

admin.site.register(BodyStyle)
admin.site.register(Car)
admin.site.register(CarInstance)
admin.site.register(Brand)
