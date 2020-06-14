from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('read_task')
    return render(request, 'task_form.html', {'form' : form})

def read_task(request):
    tasks = Task.objects.all()
    return render(request, 'task_read.html', {'tasks' : tasks})


def update_task(request, id):
    task = Task.objects.get(pk = id)
    form = TaskForm(request.POST or None, instance = task)
    if form.is_valid():
        form.save()
        return redirect('read_task')
    return render(request, 'task_form.html', {'form' : form})

def delete_task(request, id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('read_task')