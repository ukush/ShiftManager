from django import forms
from .models import ShiftPattern, ShiftAssignment, User


class ShiftPatternForm(forms.ModelForm):
    class Meta:
        model = ShiftPattern
        fields = ['name', 'department', 'start_time', 'end_time']
        labels = {'name': 'Shift Pattern', 'department': 'Department', 'start_time': 'Start', 'end_time': 'End'}

# class ShiftForm(forms.ModelForm):
#     class Meta:
#         model = Shift
#         fields = ['shift_start', 'shift_end', 'pattern', 'manager']
#         fields = {'shift_start':'Date Start', 'shift_end':'Date End', 'pattern':'Shift Pattern', 'manager':'Shift Manager'}

class GenerateDatesForm(forms.Form):
    shift_start_date = forms.DateField(
        label="Start",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
        )
    shift_end_date = forms.DateField(
        label="End",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
        )

class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = ['user']
        labels = {'user': 'Assigned User'}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'telephone', 'department', 'role']
        labels = {'name': 'Name', 'telephone': 'Phone', 'department': 'Department', 'role': 'Role'}