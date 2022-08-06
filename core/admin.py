from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.model.user import User
from django.contrib.auth.models import Group

#admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

from rest_framework.authtoken.admin import (
    TokenProxy
)

admin.site.unregister(TokenProxy)