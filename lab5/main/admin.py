from django.contrib import admin
from main.models import List, Task


class TaskInline(admin.TabularInline):
    model = Task


class ListAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]
    list_filter = ['name']
    search_fields = ['name']


class TaskAdmin(admin.ModelAdmin):
    list_filter = ['created', 'due_on', 'mark']
    search_fields = ['name', 'owner']


admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)
