# Generated by Django 3.1.7 on 2021-03-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210314_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsurvivor',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
