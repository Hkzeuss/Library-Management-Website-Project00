from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username