# Generated by Django 3.1.7 on 2021-08-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_postimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='images',
            field=models.ImageField(upload_to='uploaded_images/'),
        ),
    ]
