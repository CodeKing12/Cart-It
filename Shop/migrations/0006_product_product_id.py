# Generated by Django 3.1.7 on 2021-08-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20210419_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.SlugField(default='rffdssss'),
            preserve_default=False,
        ),
    ]
