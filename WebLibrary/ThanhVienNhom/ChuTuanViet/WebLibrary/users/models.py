from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=50)
    
