from django.contrib import admin
from .models import Subject, Assignment


# Register models in Django Admin
admin.site.register(Subject)
admin.site.register(Assignment)