from django.db import models
from django.db import models
from django.urls import reverse

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Enter the user's name")
    dob = models.DateField(help_text="Enter the user's date of birth")
    role = models.CharField(max_length=50, help_text="Enter the user's role")

    def __str__(self):
        return self.name
