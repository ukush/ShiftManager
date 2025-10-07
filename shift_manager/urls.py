"""Defines URL Patterns for Shift Manager"""

from django.urls import path

from . import views

appname = "shift_manager"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all users
    path('users/', views.users, name='users'),
    # Page that shows single user
    path('users/<int:user_id>/', views.user, name='user'),
    # Page that shows individual user's shifts
    path('users/<int:user_id>/shifts', views.user_shifts, name='user_shifts')
]