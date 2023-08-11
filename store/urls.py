from django.contrib import admin
from django.urls import path
from . views import Index, Details

app_name = "store"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('details/<int:pk>', Details.as_view(), name="details"),
]