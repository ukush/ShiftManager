from django import forms
from .models import ShiftPattern, Shift, Assignment


class ShiftPatternForm(forms.ModelForm):
    class Meta:
        model = ShiftPattern
        fields = ['name', 'department', 'start_time', 'end_time']
        labels = {'name': 'Shift Pattern', 'department': 'Department', 'start_time': 'Start', 'end_time': 'End'}

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['shift_start', 'shift_end', 'pattern', 'manager']
        fields = {'shift_start':'Date Start', 'shift_end':'Date End', 'pattern':'Shift Pattern', 'manager':'Shift Manager'}

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['user', 'shift']
        labels = {'user': 'Assigned User', 'shift': 'Shift'}