# Generated by Django 2.0.3 on 2019-01-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20190128_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='sequence',
            field=models.CharField(default=0.00045559973492379055, max_length=10),
            preserve_default=False,
        ),
    ]