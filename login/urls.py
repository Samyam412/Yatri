from itertools import product
from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product import views

from . import views

urlpatterns = [
    path('/', views.login, name="login"),
    path('logout', views.signout, name="signout"),
]