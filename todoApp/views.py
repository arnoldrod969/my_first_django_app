from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def home(request):
    task = Task.objects.all()
    taskform = TaskForm
    context = {
        'tasks': task,
        'taskform': taskform
    }
    return render(request, 'home.html', context)


def addtask(request):
    taskform = TaskForm(request.POST)
    if taskform.is_valid():
        taskform.save()
        
    return redirect('home')


def update(request, pk):
    task = Task.objects.get(id=pk)
    taskform = TaskForm(instance=task)
    context = {
        'tasks': task,
        'taskform': taskform
    }
    return render(request, 'update.html', context)


def updatetask(request, pk):
    taskform = TaskForm(request.POST, instance=Task.objects.get(id=pk))
    if taskform.is_valid():
        taskform.save()
        return redirect('home')


def delete(request, pk):
    task = Task.objects.get(id=pk)
    taskform = TaskForm
    context = {
        'tasks': task,
        'taskform': taskform
    }
    return render(request, 'delete.html', context)


def deletetask(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('home')
