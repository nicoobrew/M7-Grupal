from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.view_login, name="login"),
]