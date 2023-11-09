from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='Hãy điền họ của bạn tại đây!', max_length=50)
    last_name = models.CharField(default='Hãy điền tên của bạn tại đây!', max_length=50)
    desc = models.CharField(default='Hãy giới thiệu về bản thân mình thêm nhé!', max_length=200)
    profile_img = models.ImageField(default='media/avatar.jpg', upload_to='media', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"