# Generated by Django 4.1 on 2022-08-08 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lego',
            old_name='minimumage',
            new_name='minimum_age',
        ),
    ]
