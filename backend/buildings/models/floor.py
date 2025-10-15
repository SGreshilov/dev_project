from django.db import models

from projects.models import Project

from .building import Building
from .section import Section


class Floor(models.Model):
    """
    Модель этажа
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Корпус'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Секция/подъезд'
    )
    number = models.IntegerField()
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'