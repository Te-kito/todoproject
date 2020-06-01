from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    model = TodoModel
    template_name = 'list.html'

class TodoDetail(DetailView):
    model = TodoModel
    template_name = 'detail.html'

class TodoCreate(CreateView):
    model = TodoModel
    template_name = 'create.html'
    fields = ('title', 'memo', 'priority', 'duedate')
    # TODO class内ではreverse_lazy(), funcではreverse()
    # ? reverseとは逆にするという意味。urlを逆回りするということ。
    # ? つまり、URLからVIEWを指定するのではなく、VIEWからURLを指定する関数
    success_url = reverse_lazy('list')   

class TodoDelete(DeleteView):
    model = TodoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list') 

class TodoUpdate(UpdateView):
    model = TodoModel
    template_name = 'update.html'
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')   