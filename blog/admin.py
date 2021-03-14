from django.contrib import admin

from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Car, CarAdmin)