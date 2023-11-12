# Generated by Django 4.2.6 on 2023-11-12 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_book_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borrow', '0002_remove_borrow_book_remove_borrow_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]