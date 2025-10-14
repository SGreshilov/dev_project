from django.db import models

from projects.models import Project


class Building(models.Model):
    """
    Модель корпуса
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    number = models.IntegerField()
    commission_date = models.DateField()