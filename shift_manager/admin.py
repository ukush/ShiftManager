from django.contrib import admin

# Register your models here.

from .models import User, Role, Department, ShiftAssignment, ShiftPattern
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(ShiftAssignment)
admin.site.register(ShiftPattern)

