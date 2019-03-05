from django.views import generic
from .models import Debate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from django.urls.base import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'politics/index.html'
    
    def get_queryset(self):
        return Debate.objects.all()
    
class DetailView(generic.DetailView):
    model = Debate
    template_name = 'politics/detail.html'
    
class DebateCreate(CreateView):
    model = Debate
    fields = ['username','title', 'description']
    
class DebateUpdate(UpdateView):
    model = Debate
    fields = ['username','title', 'description']

class DebateDelete(DeleteView):
    model = Debate
    success_url = reverse_lazy('politics:index')

