from django.db import models

from projects.models import Project

from buildings.models.building import Building
from buildings.models.section import Section
from buildings.models.floor import Floor

from .constants import PROPERTY_STATUS_CHOICES, PROPERTY_TYPE_CHOICES


class Property(models.Model):
    """
    Модель объекта собственности
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Корпус'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Секция/подъезд'
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Этаж'
    )
    number = models.IntegerField(verbose_name='Номер')
    area = models.CharField(max_length=64, verbose_name='Местоположение')
    price = models.IntegerField(verbose_name='Цена')
    status = models.CharField(
        choices=PROPERTY_STATUS_CHOICES,
        max_length=64,
        verbose_name='Статус'
    )
    type = models.CharField(
        choices=PROPERTY_TYPE_CHOICES,
        max_length=64,
        verbose_name='Тип помещения'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Объект собственности'
        verbose_name_plural = 'Объекты собственности'
