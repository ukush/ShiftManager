"""Defines URL Patterns for Shift Manager"""

from django.urls import path

from . import views

app_name = "shift_manager"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all users
    path('users/', views.users, name='users'),
    # Page that shows single user
    path('users/<int:user_id>/', views.user, name='user'),
    # Page to create new users
    path('users/create', views.user_create, name='user_create'),
    # Page that shows all assigned shifts
    path('shifts/', views.shifts, name='shifts'),
    # Page that shows individual user's shifts
    path('users/<int:user_id>/shifts/', views.user_shifts, name='user_shifts'),
    # Page to create shift patterns
    path('shifts/create/pattern', views.create_shift_pattern, name='create_shift_pattern'),
    # Page to display shift patterns
    path('shifts/patterns/', views.shift_pattern, name='shift_pattern'),
    # Page to crate shifts
    path('shifts/generate/', views.generate_dates, name='generate_dates'),
    # Page to create shifts
    path('shifts/create/', views.create_shift, name='create_shift')
]