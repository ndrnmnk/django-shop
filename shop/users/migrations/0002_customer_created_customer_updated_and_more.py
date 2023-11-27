# Generated by Django 4.2.6 on 2023-11-22 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last updated'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='login',
            field=models.CharField(max_length=50, verbose_name='Your login'),
        ),
    ]
