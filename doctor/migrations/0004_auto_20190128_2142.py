# Generated by Django 2.0.3 on 2019-01-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20190128_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='cat_name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='subcatagory',
            old_name='cat_name',
            new_name='category_name',
        ),
    ]
