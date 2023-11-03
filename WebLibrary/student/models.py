from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='pham', max_length=20)
    last_name = models.CharField(default='manh', max_length=20)
    desc = models.CharField(default='toilalaptrinhvien', max_length=200)
    profile_img = models.ImageField(default='media/avatar.jpg', upload_to='media', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"