from django.shortcuts import render

from rest_framework import viewsets

from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet проектов ЖК"""

    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectDetailSerializer