# Generated by Django 4.1.5 on 2023-02-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pic.png', upload_to=''),
        ),
    ]