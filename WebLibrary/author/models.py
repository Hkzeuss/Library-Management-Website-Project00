from django.db import models
from django.urls import reverse

# # Create your models here.


class Author(models.Model):
    title = models.CharField(max_length=200)
    # student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('author:detail', args=[str(self.id)])