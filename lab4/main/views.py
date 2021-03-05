"""
    This views show Function-Based-View(FBV).
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm, ListForm
from .models import List, Task


def show_task_list_view(request, pk):
    data = Task.objects.filter(list_id=pk, mark=False)
    return render(request, 'todo/todo_list.html', {"data": data, 'number': pk})


def show_task_completed_list_view(request, pk):
    data = Task.objects.filter(list_id=pk, mark=True)
    return render(request, 'todo/todo_completed_list.html', {"data": data, 'number': pk})


def change_mark(request, pk):
    task = Task.objects.get(id=pk)
    if task.mark is True:
        task.mark = False
        task.save()
        return redirect('todos_completed', pk=task.list_id)
    elif task.mark is False:
        task.mark = True
        task.save()
        return redirect('todos', pk=task.list_id)
    return HttpResponse("Everything OK :)")


def show_list_view(request):
    data = List.objects.all()
    return render(request, 'todo/list_page.html', {"data": data})


def task_form_view(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to='tasks')
    return render(request, 'todo/task_add_form.html', {'form': form})


def list_form_view(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to='tasks')
    return render(request, 'todo/task_add_form.html', {'form': form})


def delete_list(request, pk):
    deleted_list = List.objects.get(id=pk)
    deleted_list.delete()
    return redirect("tasks")
