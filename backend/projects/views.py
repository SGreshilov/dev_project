from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from buildings.serializer import BuildingSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet проектов ЖК"""

    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectDetailSerializer

    @action(detail=True)
    def buildings(self, request, pk=None):
        project = self.get_object()
        serializer = BuildingSerializer(project.buildings.all(), many=True)
        return Response(serializer.data)