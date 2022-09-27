# Generated by Django 2.0.3 on 2019-02-01 06:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20190129_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='myAword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aword_title', models.CharField(blank=True, max_length=100)),
                ('aword_year', models.CharField(blank=True, max_length=100)),
                ('for_aword', models.CharField(blank=True, max_length=100)),
                ('place', models.CharField(blank=True, max_length=100)),
                ('aword_details', ckeditor.fields.RichTextField()),
                ('aword_images', models.ImageField(upload_to='images/aword')),
                ('status', models.BooleanField(default=True)),
                ('aword_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
