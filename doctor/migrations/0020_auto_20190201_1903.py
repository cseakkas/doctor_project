# Generated by Django 2.0.3 on 2019-02-01 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_auto_20190201_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryinfo',
            old_name='gallery_for',
            new_name='gallery_category',
        ),
    ]
