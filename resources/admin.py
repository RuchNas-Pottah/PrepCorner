from django.contrib import admin

# Register your models here.
from .models import Resources,Resource
admin.site.register(Resources)
admin.site.register(Resource)