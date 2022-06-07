from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lp, name = "lp"),
    path('lps', views.lps, name = "lps"),
]
