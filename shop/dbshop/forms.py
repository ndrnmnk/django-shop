from .models import Goods
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['title', 'description', 'price', 'updated', 'pic', 'author']

        labels = {
            'title': '',
            'description': '',
            'price': '',
            'updated': '',
            'pic': '',
            'author': '',
            }

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of good'}),
            "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of a good'}),
            "price": TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in USD'}),
            "updated": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Current date and time'}),
            "author": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Your login'}),
        }
