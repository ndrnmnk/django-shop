# Generated by Django 4.2.6 on 2023-11-01 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Good', 'verbose_name_plural': 'Goods'},
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='name',
            new_name='title',
        ),
    ]
