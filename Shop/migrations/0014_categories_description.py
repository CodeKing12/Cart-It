# Generated by Django 3.1.7 on 2021-08-09 15:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_categories_category_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
