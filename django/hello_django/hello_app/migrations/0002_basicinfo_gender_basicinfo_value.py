# Generated by Django 4.2.11 on 2024-04-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='gender',
            field=models.CharField(default='M', max_length=5),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='value',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]