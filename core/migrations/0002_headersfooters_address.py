# Generated by Django 3.1 on 2022-01-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersfooters',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
