from django.contrib import admin
from .models import Animal

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display=('id','name','genus','is_domesticated')

admin.site.register(Animal, AnimalAdmin)