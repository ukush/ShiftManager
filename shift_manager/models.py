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
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    pattern = models.ForeignKey(ShiftPattern, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, related_name='managed_assignments', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date', 'pattern')
