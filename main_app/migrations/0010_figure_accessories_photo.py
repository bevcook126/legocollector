# Generated by Django 4.1 on 2022-08-11 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_lego_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure',
            name='accessories',
            field=models.CharField(default='accessory', max_length=100),
            preserve_default=False,

        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lego')),
            ],
        ),
    ]