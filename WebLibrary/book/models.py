from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from category.models import Category
from WebLibrary import settings
from django.contrib.auth.models import User
from author.models import Author
from django.core.validators import MinValueValidator

# Create your models here.


class Book(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="books", null=True)
    translater = models.CharField(max_length=200,null=True)
    publisher = models.CharField(max_length=200,null=True)
    page = models.CharField(max_length=200,null=True)
    Publication_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    # student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="books", null=True)
    student = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, related_name="books", null=True, blank=True)
    description = models.TextField()
    img = models.ImageField(default='book/images/Background_1.jpg', upload_to='book/images/', null=True, blank=True)
    pdf = models.FileField(upload_to='book/pdfs/', null=True, blank=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)], default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('book:book_detail', args=[str(self.pk)])