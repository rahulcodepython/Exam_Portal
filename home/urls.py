from django.urls import path
from home import views

urlpatterns = [

    path('', views.login_temp, name="login_temp"),
    path('login_user', views.login_user, name="login_user"),
    path('register_temp', views.register_temp, name="register_temp"),
    path('register', views.register, name="register"),

    path('submit', views.submit, name="submit"),
    path('dashboard', views.dashboard, name="dashboard"),

]
