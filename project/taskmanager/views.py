from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .models import Task
from .serializers import TaskSerializer, TaskAddSerializer, TaskDeleteSerializer, TaskEditSerializer


class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAdd(CreateAPIView):
    serializer_class = TaskAddSerializer


class TaskDelete(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteSerializer


class TaskEdit(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEditSerializer
