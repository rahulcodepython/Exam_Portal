from django.contrib import admin
from home.models import Custom_User


class Custom_User_Admin(admin.ModelAdmin):
    model = Custom_User
    list_display = ['user']


admin.site.register(Custom_User, Custom_User_Admin)
