from socket import fromshare
from django import forms 
from todo.models import TodoApp

class TodoAppForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['title', 'description']