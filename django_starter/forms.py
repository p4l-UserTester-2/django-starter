from django.forms import ModelForm
from django_starter.models import Task

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['content']
