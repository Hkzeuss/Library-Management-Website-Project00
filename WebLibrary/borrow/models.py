from django.db import models
from django.urls import reverse

class Borrow(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f'{self.borrow_date} - {self.return_date}'

    def get_absolute_url(self):
        return reverse('borrow:borrow-detail', args=[str(self.id)])