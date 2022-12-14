# Generated by Django 2.0.3 on 2019-02-19 16:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_auto_20190201_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_title', models.CharField(blank=True, max_length=100)),
                ('program_details', ckeditor.fields.RichTextField()),
                ('program_place', models.CharField(blank=True, max_length=100)),
                ('program_image', models.ImageField(upload_to='images/program_image')),
                ('program_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'My Program',
                'verbose_name_plural': 'My Programs',
            },
        ),
    ]
