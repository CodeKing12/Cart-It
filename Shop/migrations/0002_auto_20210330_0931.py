# Generated by Django 3.1.7 on 2021-03-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='Shop.Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
