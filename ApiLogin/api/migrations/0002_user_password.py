# Generated by Django 3.2.4 on 2021-11-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=141198, max_length=25, verbose_name='Contraseña'),
            preserve_default=False,
        ),
    ]