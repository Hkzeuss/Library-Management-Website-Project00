# Generated by Django 4.2.5 on 2023-11-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_rename_username_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='avatar.jpg', upload_to='upload_avatar'),
        ),
    ]
