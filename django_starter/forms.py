from django.forms import ModelForm, TextInput
from django_starter.models import Task

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['content']
    widgets = {
      'content': TextInput(attrs={'autofocus': 'autofocus', 'placeholder': 'Add a Todo!'}),
    }
