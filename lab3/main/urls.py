from django.urls import path

from main.views import show_task_list, show_task_completed_list

urlpatterns = [
    path('todos/', show_task_list, name='todos'),
    path('todos/<int:pk>/completed', show_task_completed_list, name='todos_completed')
]