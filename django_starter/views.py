#  from django.http import HttpResponse
from django.forms import modelformset_factory
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django_starter.models import Task
from django_starter.forms import TaskForm

class TaskView(View):
    template_name = 'index.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'tasks': list(Task.objects.all()), 'form': form})

    def post(self, request, **opts):
        if 'task_id' in opts and opts['task_id']:
            task = get_object_or_404(Task, pk=opts['task_id'])
            task.delete()
        else:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('view-tasks')
