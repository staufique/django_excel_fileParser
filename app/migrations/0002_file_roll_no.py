# Generated by Django 4.2.4 on 2023-12-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='roll_no',
            field=models.IntegerField(default=None),
        ),
    ]
