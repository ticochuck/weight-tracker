from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Weights


class HomePageView(ListView):
    template_name = 'home.html'
    model = Weights
    

class CreatePageView(CreateView):
    template_name = 'create.html'
    model = Weights
    fields = '__all__'


class DetailPageView(DetailView):
    template_name = 'detail_view.html'
    model = Weights


class UpdatePageView(UpdateView):
    template_name = 'update.html'
    fields = '__all__'
    model = Weights


class DeletePageView(DeleteView):
    template_name = 'delete.html'
    model = Weights
    success_url = reverse_lazy('home')
