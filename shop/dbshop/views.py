from django.shortcuts import render, redirect
from .models import Goods
from .forms import GoodsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from datetime import datetime
from django.db import models


def search(request):
    good = Goods.objects.order_by('title')
    return render(request, 'dbshop/search.html', {'good': good})


class GoodsDetailView(DetailView):
    model = Goods
    template_name = 'dbshop/detail_view.html'
    context_object_name = 'good'


class GoodsUpdateView(UpdateView):
    model = Goods
    template_name = 'dbshop/create.html'
    form_class = GoodsForm


class GoodsDeleteView(DeleteView):
    model = Goods
    success_url = '/shopping'
    template_name = 'dbshop/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.updated = datetime.now()
            form.save()
            return redirect('home')
        else:
            error = "Invalid form!"
    form = GoodsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'dbshop/create.html', data)
