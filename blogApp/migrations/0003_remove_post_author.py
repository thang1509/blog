# Generated by Django 3.1.6 on 2021-05-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20210525_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
