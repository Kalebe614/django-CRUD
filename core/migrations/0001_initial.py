# Generated by Django 4.2.2 on 2023-06-30 11:52

import core.models
from django.db import migrations, models
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('activity', models.BooleanField(default=True, verbose_name='Activity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('picture', pictures.models.PictureField(aspect_ratios=[None, '1/1', '3/2', '16/9'], blank=True, breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, pixel_densities=[1, 2], upload_to=core.models.getFilename)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]