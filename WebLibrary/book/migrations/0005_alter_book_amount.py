# Generated by Django 4.2.6 on 2023-11-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_amount_alter_book_author_alter_book_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amount',
            field=models.CharField(max_length=200, null=True),
        ),
    ]