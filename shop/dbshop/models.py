from django.db import models


class Goods(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('Description', max_length=2000)
    created = models.DateTimeField('Created at', auto_now_add=True)
    updated = models.DateTimeField('Last updated')
    author = models.CharField('Created by', max_length=50)
    pic = models.ImageField('Picture of a good', default='404.webp', upload_to='uploads')
    price = models.FloatField('Price in USD')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/shopping/{self.id}'

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'
