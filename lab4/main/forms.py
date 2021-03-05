from django import forms

from main.models import Task, List


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "due_on", 'owner', 'list']


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
