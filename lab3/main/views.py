from django.shortcuts import render


def show_task_list(request):
    data = [
        {'name': 'Task 1', 'created': '10/09/2018', 'due_on': '12/09/2018', 'owner': 'admin', 'mark': False},
        {'name': 'Task 2', 'created': '10/09/2019', 'due_on': '12/09/2019', 'owner': 'admin', 'mark': False},
        {'name': 'Task 3', 'created': '10/09/2020', 'due_on': '12/09/2020', 'owner': 'admin', 'mark': False},
        {'name': 'Task 4', 'created': '10/09/2021', 'due_on': '12/09/2021', 'owner': 'admin', 'mark': False}
    ]

    return render(request, 'todo/todo_list.html', {"data": data})


def show_task_completed_list(request, pk):
    data = [
        {'name': 'Task 1', 'created': '10/09/2018', 'due_on': '12/09/2018', 'owner': 'admin', 'mark': True},
    ]

    return render(request, 'todo/todo_completed_list.html', {"data": data, 'number': pk})
