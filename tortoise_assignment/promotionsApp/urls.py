from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path('plan/', PlanView.as_view()),
    path('user/', UserView.as_view())

]
