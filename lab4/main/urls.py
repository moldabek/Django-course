from django.urls import path

from main.views import show_task_list_view, show_task_completed_list_view, show_list_view, change_mark

urlpatterns = [
    path('todos/', show_list_view, name='tasks'),
    path('todos/<int:pk>', show_task_list_view, name='todos'),
    path('change/<int:pk>', change_mark, name='change'),
    path('todos/<int:pk>/completed', show_task_completed_list_view, name='todos_completed')
]