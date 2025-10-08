from django.db import models

# Create your models here.

class Department(models.Model):
    """The department which a user works in"""
    name = models.CharField(50)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Return a string representation of the Role model"""
        return self.name

class Role(models.Model):
    """The role of a user, dictating their site priviledges"""
    name = models.CharField(20)

    def __str__(self):
        """Return a string representation of the Role model"""
        return self.name

class User(models.Model):
    """A user of the app"""
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=11)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Role, default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    

class ShiftPattern(models.Model):
    name = models.CharField(max_length=50)
    shift_start = models.DateTimeField()
    shift_end = models.DateTimeField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.start_time}-{self.end_time}"

class Shift(models.Model):
    pattern = models.ForeignKey(ShiftPattern, on_delete=models.CASCADE)
    date = models.DateField()
    manager = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('pattern', 'date')


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'shift')
