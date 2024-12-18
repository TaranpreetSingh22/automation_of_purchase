from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('rg', 'Registrar'),
        ('hod', 'HOD'),
        ('VC', 'Vice Chancellor'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='admin')
    email = models.EmailField(unique=True)  # Enforcing unique email
