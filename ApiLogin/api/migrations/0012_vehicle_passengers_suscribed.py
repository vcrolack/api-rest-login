# Generated by Django 3.2.4 on 2021-12-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='passengers_suscribed',
            field=models.IntegerField(default=0, verbose_name='Pasajeros suscritos'),
            preserve_default=False,
        ),
    ]