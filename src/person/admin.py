from django.contrib import admin

# Import the model
from .models import Person

# Register your models here.
admin.site.register(Person)
