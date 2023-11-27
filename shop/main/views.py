from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

def error(request):
    return render(request, 'main/error.html')
