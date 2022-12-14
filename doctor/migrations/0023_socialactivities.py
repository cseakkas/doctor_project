# Generated by Django 2.0.3 on 2019-02-19 18:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0022_academicqualification_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('details', ckeditor.fields.RichTextField()),
                ('place', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('program_image', models.ImageField(upload_to='images/program_image')),
                ('program_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Activities',
                'verbose_name_plural': 'Social Activities',
            },
        ),
    ]
