from django.db import models

from projects.models import Project

from .building import Building


class Section(models.Model):
    """
    Модель секции/подъезда
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='sections')
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name='sections')
    number = models.IntegerField()
    floor_count = models.IntegerField()