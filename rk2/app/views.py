from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import *
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def report(request):
    files = File.objects.all()
    return render(request, 'report.html', {'files': files, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})


def catalog_list(request):
    catalogs = Catalog.objects.all().values()
    return render(request, 'list.html', {'entity': 'Catalog', 'objects': catalogs})


def file_list(request):
    files = File.objects.all().values()
    return render(request, 'list.html', {'entity': 'File', 'objects': files})


class CatalogCreate(CreateView):
    model = Catalog
    fields = ['name']
    success_url = '/catalog'
    template_name = 'catalog_form.html'


class CatalogUpdate(UpdateView):
    model = Catalog
    fields = ['name']
    success_url = '/catalog'
    pk_url_kwarg = 'id'
    template_name = 'catalog_form.html'


class CatalogDelete(DeleteView):
    model = Catalog
    success_url = '/catalog'
    pk_url_kwarg = 'id'
    template_name = 'catalog_delete_form.html'


class FileCreate(CreateView):
    model = File
    fields = ['name', 'size', 'extension', 'catalog']
    success_url = '/file'
    template_name = 'file_form.html'


def get_context_data(self, **kwargs):
    context = super(FileCreate, self).get_context_data(**kwargs)
    context['form'].fields['catalog'] = forms.ModelChoiceField(queryset=Catalog.objects.all(),
                                                               empty_label=None, label='Каталог')
    return context


class FileUpdate(UpdateView):
    model = File
    fields = ['name', 'size', 'extension', 'catalog']
    pk_url_kwarg = 'id'
    success_url = '/file'
    template_name = 'file_form.html'


def get_context_data(self, **kwargs):
    context = super(FileUpdate, self).get_context_data(**kwargs)
    context['form'].fields['catalog'] = forms.ModelChoiceField(queryset=Catalog.objects.all(),
                                                               empty_label=None, label='Каталог')
    return context


class FileDelete(DeleteView):
    model = File
    pk_url_kwarg = 'id'
    success_url = '/file'
    template_name = 'file_delete_form.html'
