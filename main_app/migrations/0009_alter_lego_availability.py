# Generated by Django 4.1 on 2022-08-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_lego_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lego',
            name='availability',
            field=models.CharField(max_length=2500),
        ),
    ]
