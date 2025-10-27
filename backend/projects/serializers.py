from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка проектов ЖК"""

    class Meta:
        model = Project
        fields = ['name', 'type']


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для одного проекта ЖК"""

    class Meta:
        model = Project
        fields = '__all__'