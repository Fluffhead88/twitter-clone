from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User, Tweet, Like

admin.site.register(User, UserAdmin)
admin.site.register(Tweet)
admin.site.register(Like) 
