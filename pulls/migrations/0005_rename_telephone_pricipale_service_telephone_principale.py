# Generated by Django 4.1.2 on 2022-10-25 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0004_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='telephone_pricipale',
            new_name='telephone_principale',
        ),
    ]
