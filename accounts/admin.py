from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Profile)