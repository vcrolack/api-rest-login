# Generated by Django 3.2.4 on 2021-11-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Correo electrónico'),
        ),
    ]
