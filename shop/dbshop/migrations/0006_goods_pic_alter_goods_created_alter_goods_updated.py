# Generated by Django 4.2.6 on 2023-11-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbshop', '0005_remove_goods_date_goods_updated_alter_goods_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='pic',
            field=models.ImageField(default='main/static/main/img/404.webp', upload_to='dbshop/uploads', verbose_name='Picture of a good'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='updated',
            field=models.DateTimeField(verbose_name='Last updated'),
        ),
    ]
