from django.db import models
from django.contrib.auth.models import User
#from multiupload.fields import MultiFileField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    desc = models.CharField( max_length=200, blank=True)
    profile_img = models.ImageField(default='media/avatar.jpg', upload_to='media', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"