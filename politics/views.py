from django.views import generic
from .models import Debate
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    
