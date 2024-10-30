from registration import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('new/', views.register, name="register")
]