# Generated by Django 4.1 on 2022-08-09 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_description_lego_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lego')),
            ],
        ),
    ]
