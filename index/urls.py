from django.contrib import admin
from django.urls import path

from index import views

urlpatterns = [
    path('', views.index),
]