from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Weights


class HomePageView(ListView):
    template_name = 'home.html'
    model = Weights
    fields = '__all__'


class CreatePageView(CreateView):
    template_name = 'home.html'
    model = Weights
    fields = '__all__'


class DetailPageView(DetailView):
    template_name = 'home.html'
    model = Weights


class UpdatePageView(UpdateView):
    template_name = 'home.html'
    model = Weights
    fields = '__all__'


class DeletePageView(DetailView):
    template_name = 'home.html'
    model = Weights
    success_url = reverse_lazy('home')
