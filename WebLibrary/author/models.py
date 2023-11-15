from django.db import models
from django.urls import reverse

# # Create your models here.

class Author(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='author/images/', default='path/to/default/image.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('author:detail', args=[str(self.id)])