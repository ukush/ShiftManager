from django.shortcuts import render
from .models import User, Assignment, Shift

def index(request):
    """The home page of the shift manager app"""
    return render(request, 'shift_manager/index.html')

def users(request):
    """The page which displays all users"""
    users = User.objects.order_by('name')
    context = {'users': users}
    return render(request, 'shift_manager/users.html', context)

def user(request, user_id):
    """The page which displays data about a single user"""
    user = User.objects.get(id=user_id)

    # Get all shifts assigned to this user
    shifts = Shift.objects.filter(assignment__user=user).order_by('shift_start')
    context = {'user': user, 'shifts': shifts}
    return render(request, 'shift_manager/user.html', context)

def user_shifts(request, user_id):
    """The page that displays an individual users' shifts to a manager"""
    user = User.objects.get(id=user_id)
    # Get all shifts assigned to this user
    shifts = Shift.objects.filter(assignment__user=user).order_by('shift_start')
    context = {'user': user, 'shifts': shifts}
    return render(request, 'shift_manager/user_shifts.html', context)



