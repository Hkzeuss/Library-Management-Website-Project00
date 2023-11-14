from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from book.models import Book

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default= None, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    borrow_date = models.DateField()
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        print(f'self.user: {self.user}')
        user_username = self.user.username if self.user else "username"
        return f'{user_username} mượn {self.book.title} từ {self.borrow_date} đến {self.return_date}'


    def get_absolute_url(self):
        return reverse('borrow:borrow-detail', args=[str(self.id)])