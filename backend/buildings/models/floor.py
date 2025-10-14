from django.db import models

from projects.models import Project

from .building import Building
from .section import Section


class Floor(models.Model):
    """
    Модель этажа
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='floors')
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name='floors')
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='floors')
    number = models.IntegerField()