# Generated by Django 2.0.3 on 2019-04-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0024_auto_20190423_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalprofile',
            name='specialist',
            field=models.CharField(blank=True, max_length=260),
        ),
        migrations.AlterField(
            model_name='personalprofile',
            name='specialist2',
            field=models.CharField(blank=True, max_length=260),
        ),
        migrations.AlterField(
            model_name='personalprofile',
            name='specialist3',
            field=models.CharField(blank=True, max_length=260),
        ),
        migrations.AlterField(
            model_name='personalprofile',
            name='specialist4',
            field=models.CharField(blank=True, max_length=260),
        ),
    ]
