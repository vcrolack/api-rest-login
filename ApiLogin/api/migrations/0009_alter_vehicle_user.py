# Generated by Django 3.2.4 on 2021-12-04 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_vehicle_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user', verbose_name='Usuario'),
        ),
    ]
