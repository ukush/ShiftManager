from django.shortcuts import render, redirect
from .models import User, ShiftAssignment, ShiftPattern
from .forms import ShiftPatternForm, GenerateDatesForm, UserForm
import datetime
from itertools import groupby
from operator import attrgetter
from collections import defaultdict

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
    shifts = ShiftAssignment.objects.filter(assignment__user=user).order_by('shift_start')
    context = {'user': user, 'shifts': shifts}
    return render(request, 'shift_manager/user.html', context)

def user_create(request):
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = UserForm()
    else:
        # POST data submitted, build form
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_manager:users')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'shift_manager/user_create.html', context)

def user_shifts(request, user_id):
    """The page that displays an individual users' shifts to a manager"""
    user = User.objects.get(id=user_id)
    # Get all shifts assigned to this user

    shifts = ShiftAssignment.objects.filter(user=user)
    context = {'user': user, 'shifts': shifts}
    return render(request, 'shift_manager/user_shifts.html', context)

def shifts(request):
    assignments = ShiftAssignment.objects.select_related('user', 'pattern', 'manager').order_by('date', 'pattern__name')

    all_shifts = []
    grouped_by_date = defaultdict(list)
    for shift in assignments:
        grouped_by_date[shift.date].append(shift)

    # Collect all unique pattern names
    unique_patterns = set()
    for shifts_for_date in grouped_by_date.values():
        for shift in shifts_for_date:
            unique_patterns.add(shift.pattern.name)

    for date, shifts_for_date in grouped_by_date.items():
        shifts_list = []
        grouped_by_pattern = defaultdict(list)
        for shift in shifts_for_date:
            grouped_by_pattern[shift.pattern.name].append(shift)

        for pattern_name, pattern_shifts in grouped_by_pattern.items():
            pattern_obj = pattern_shifts[0].pattern
            shifts_list.append({
                'pattern': {
                    'pattern_name': pattern_obj.name,
                    'pattern_department': getattr(pattern_obj, 'department', None),
                    'pattern_start': pattern_obj.start_time,
                    'pattern_end': pattern_obj.end_time,
                },
                'assigned_employees': [s.user.name for s in pattern_shifts],
                'shift_manager': pattern_shifts[0].manager.name,
            })

        all_shifts.append({
            'date': date,
            'shifts': shifts_list
        })

    context = {
        'all_shifts': all_shifts,
        'patterns': sorted(unique_patterns)  # pass patterns to template
    }
    return render(request, 'shift_manager/shifts.html', context)

def create_shift_pattern(request):
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ShiftPatternForm()
    else:
        # POST data submitted, build form
        form = ShiftPatternForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_manager:shift_pattern')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'shift_manager/create_shift_pattern.html', context)

def shift_pattern(request):
    """The page that allows a manager to create a reusable shift pattern"""
    patterns = ShiftPattern.objects.all()
    context = {'patterns': patterns}
    return render(request, 'shift_manager/shift_pattern.html', context)

def generate_dates(request):
    """The page that allows a manager to create a shift instance"""
    generated_dates = []
    patterns = ShiftPattern.objects.all()
    users = User.objects.all()

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = GenerateDatesForm()
    else:
        # POST data submitted, build form
        form = GenerateDatesForm(data=request.POST)
        if form.is_valid():
            date_start = form.cleaned_data["shift_start_date"]
            date_end = form.cleaned_data["shift_end_date"]

            delta = date_end - date_start

            for i in range(delta.days +1):
                current_day = date_start + datetime.timedelta(days=i)
                day_name = current_day.strftime("%A")
                generated_dates.append({
                    'date': current_day,
                    'day_name': day_name
                    })

    # Display blank or invalid form
    context = {'form': form, 'generated_dates': generated_dates, 'patterns': patterns, 'users': users}
    return render(request, 'shift_manager/create_shift.html', context)


def create_shift(request):
    if request.method == 'POST':
        assignments = request.POST.getlist('shift_assignment')
        
        manager = User.objects.get(id=1)


        for item in assignments:
            date_str, pattern_id, user_id = item.split('|')
            pattern = ShiftPattern.objects.get(id=pattern_id)
            user = User.objects.get(id=user_id)

            print(f'Shift Date: {date_str}')
            print(f'Shift Start: {pattern.start_time}')
            print(f'Shift End: {pattern.end_time}')
            print(f'User: {user.name}')


            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            assigned_at = datetime.datetime.now()

            # Create shift
            ShiftAssignment.objects.create(
                user=user,
                date=date_obj,
                pattern=pattern,
                manager=manager,
                assigned_at=assigned_at
            )

    return redirect('shift_manager:users') 