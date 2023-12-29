from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Folder)
class list(admin.ModelAdmin):
    list_display=['uid']
    
    
@admin.register(file)
class list(admin.ModelAdmin):
    list_display=['file']
