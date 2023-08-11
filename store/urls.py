from django.contrib import admin
from django.urls import path
from . views import Index, Details, welcome_page

app_name = "store"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('welcome', welcome_page, name='welcome'),
    path('details/<int:pk>', Details.as_view(), name='details'),
]