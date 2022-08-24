from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from todo.models import TodoApp
from todo.forms import TodoAppForm
from django.urls import reverse_lazy

# Create your views here.
class TodoAppCreateView(CreateView):
    model = TodoApp
    form_class = TodoAppForm
    template_name = 'home.html'

class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'todo.html'
    context_object_name = 'todos'

class TodoAppDetailView(DetailView):
    model = TodoApp
    context_object_name = 'todo'
    template_name = 'todo_detail.html'

class TodoAppUpdateView(UpdateView):
    model = TodoApp
    form_class = TodoAppForm
    template_name = 'home.html'

class TodoAppDeleteView(DeleteView):
    model = TodoApp
    success_url = reverse_lazy('todo')
    template_name = 'todo_delete.html'