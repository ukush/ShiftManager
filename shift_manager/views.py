from django.shortcuts import render
from .models import User

def index(request):
    """The home page of the shift manager app"""
    return render(request, 'shift_manager/index.html')


def users(request):
    """The page which displays all users"""
    users = User.objects.order_by('name')
    context = {'users': users}
    return render(request, 'shift_manager/users.html', context)