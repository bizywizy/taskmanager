from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskAddSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('text',)


class TaskDeleteSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',)


class TaskEditSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('text',)
