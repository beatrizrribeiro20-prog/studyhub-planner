from django.db import models
from django.contrib.auth.models import User


# Subject model stores school subjects
class Subject(models.Model):

    # User who owns the subject
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Subject name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Assignment model stores assignments/tasks
class Assignment(models.Model):

    # User who owns the assignment
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Assignment title
    title = models.CharField(max_length=200)

    # Assignment description
    description = models.TextField()

    # Completion status
    completed = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title