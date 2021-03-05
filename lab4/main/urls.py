from django.urls import path

from main.views import show_task_list_view, show_task_completed_list_view, show_list_view, change_mark, \
    task_form_view, list_form_view, delete_list

urlpatterns = [
    path('todos/', show_list_view, name='tasks'),
    path('todos/<int:pk>', show_task_list_view, name='todos'),
    path('change/<int:pk>', change_mark, name='change'),
    path('todos/<int:pk>/completed', show_task_completed_list_view, name='todos_completed'),
    path('add_task/', task_form_view, name='task_form'),
    path('add_list/', list_form_view, name='list_form'),
    path('delete/<int:pk>', delete_list, name='delete')
]