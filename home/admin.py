from django.contrib import admin

# Register your models here.

from home.models import Questions, Custom_User

class Question_Admin(admin.ModelAdmin):
    model = Questions
    list_display = ['question', 'id_no', 'category', 'correct']


class Custom_User_Admin(admin.ModelAdmin):
    model = Custom_User
    list_display = ['user']

admin.site.register(Custom_User, Custom_User_Admin)
admin.site.register(Questions, Question_Admin)
