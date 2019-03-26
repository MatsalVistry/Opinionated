from django.views import generic
from .models import Debate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
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
    
def post_detail(request, id, slug):
    post=get_object_or_404(Debate,id=id,slug=slug)
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True;
    context = {
        'post':post,
        'is_liked': is_liked,
        }
    return render(request, 'politics/detail.html',context)
def like_debate(request):
    post = get_object_or_404(Debate, id=request.POST.get('debate_id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked= False
    else:
        post.likes.add(request.user)
        is_liked= True
    return HttpResponseRedirect(post.get_absolute_url())

