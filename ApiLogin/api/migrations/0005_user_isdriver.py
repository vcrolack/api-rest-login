# Generated by Django 3.2.4 on 2021-12-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isDriver',
            field=models.CharField(default='false', max_length=10, verbose_name='Conductor'),
        ),
    ]
