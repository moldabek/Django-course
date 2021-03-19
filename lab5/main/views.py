from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.serializers import TaskSerializer, ListSerializer, TodoGetSerializer
from main.models import List, Task
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q, Prefetch


class TodoListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = List.objects.all()
    serializer_class = ListSerializer


class TodoIncompleteRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        import pdb
        pdb.set_trace()
        return Task.objects.filter(list_id=self.kwargs.get("pk"), mark=True)


class TodoCompleteRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        import pdb
        pdb.set_trace()
        return Task.objects.filter(list_id=self.kwargs.get("pk"), mark=False)


class TaskListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
