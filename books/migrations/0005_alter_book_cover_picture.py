# Generated by Django 4.1.5 on 2023-02-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='default_cover.png', upload_to=''),
        ),
    ]
