# Generated by Django 3.1.6 on 2021-05-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0012_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]
