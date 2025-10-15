from django.db import models

from projects.models import Project

from .building import Building


class Section(models.Model):
    """
    Модель секции/подъезда
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='sections',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='sections',
        verbose_name='Корпус'
    )
    number = models.IntegerField(verbose_name='Номер')
    floor_count = models.IntegerField(verbose_name='Количество этажей')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Секция/подъезд'
        verbose_name_plural = 'Секции/подъезды'
