# Generated by Django 3.1.7 on 2021-04-17 20:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
