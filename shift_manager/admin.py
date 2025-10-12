from django.contrib import admin

# Register your models here.

from .models import User, Role, Department, Shift, Assignment, ShiftPattern
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Shift)
admin.site.register(Assignment)
admin.site.register(ShiftPattern)

