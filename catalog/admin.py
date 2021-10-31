from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from .models import BodyStyle, Car, CarInstance, Brand

# Register your models here.

admin.site.register(BodyStyle)
admin.site.register(Car)
admin.site.register(CarInstance)
admin.site.register(Brand)

class CarInstanceAdmin(admin.ModelAdmin):
    list_display = ('car', 'status', 'renter', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
                 (None, 
                        {'fields': ('car', 'plate', 'id')}),
                 ('Availability',
                        {'fields': ('status', 'due_back', 'renter')})
                )