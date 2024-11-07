from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)