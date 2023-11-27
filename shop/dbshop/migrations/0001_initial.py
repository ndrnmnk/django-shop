# Generated by Django 4.2.6 on 2023-11-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
                ('date', models.DateTimeField(verbose_name='Date of publication')),
                ('price', models.IntegerField(verbose_name='Price in cents')),
            ],
        ),
    ]