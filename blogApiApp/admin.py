from django.contrib import admin
from . import models

# We register models, so we can view them in Django admin Dashboard
# After this we need to create a superuser to access admin dashboard
# python3 manage.py createsuperuser
admin.site.register(models.Post)
