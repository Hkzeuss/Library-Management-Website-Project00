# Generated by Django 4.2.5 on 2023-11-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='media/avatar.jpg', upload_to='media'),
        ),
    ]
