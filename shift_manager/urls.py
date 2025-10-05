"""Defines URL Patterns for Shift Manager"""

from django.urls import path

from . import views

appname = "shift_manager"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all users
    path('users/', views.users, name='users')
]