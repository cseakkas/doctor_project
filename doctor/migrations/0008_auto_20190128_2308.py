# Generated by Django 2.0.3 on 2019-01-28 17:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_name', models.CharField(blank=True, max_length=100)),
                ('operation_title', models.CharField(blank=True, max_length=100)),
                ('operation_details', ckeditor.fields.RichTextField()),
                ('after_images', models.ImageField(upload_to='images/operations')),
                ('before_images', models.ImageField(upload_to='images/operations')),
                ('status', models.BooleanField(default=True)),
                ('operation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Operation Post',
                'verbose_name_plural': 'Add Operation Post',
            },
        ),
        migrations.RemoveField(
            model_name='operation',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcatagory',
            name='category_name',
        ),
        migrations.RenameModel(
            old_name='Catagory',
            new_name='OperationCatagory',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
        migrations.DeleteModel(
            name='SubCatagory',
        ),
        migrations.AddField(
            model_name='operationpost',
            name='operation_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.OperationCatagory'),
        ),
    ]
