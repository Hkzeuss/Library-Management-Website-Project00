# Generated by Django 4.2.5 on 2023-11-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desc',
            field=models.CharField(default='Hãy giới thiệu về bản thân mình thêm nhé!', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Hãy điền họ của bạn tại đây!', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Hãy điền tên của bạn tại đây!', max_length=20),
        ),
    ]
