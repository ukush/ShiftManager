from django.shortcuts import render, redirect
from .models import User, Assignment, Shift
from .forms import ShiftPatternForm

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

def create_shift_pattern(request):
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ShiftPatternForm()
    else:
        # POST data submitted, build form
        form = ShiftPatternForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_manager:users')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'shift_manager/create_shift_pattern.html', context)

