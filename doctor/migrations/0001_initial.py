# Generated by Django 2.0.3 on 2019-01-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SubCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=50)),
                ('details', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=1)),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Catagory')),
            ],
        ),
    ]
