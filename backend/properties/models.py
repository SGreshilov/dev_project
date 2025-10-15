from django.db import models

from .constants import PROPERTY_STATUS_CHOICES, PROPERTY_TYPE_CHOICES


class Property(models.Model):
    """
    Модель объекта собственности
    """
    project = models.ForeignKey(
        to='projects.Project',
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        to='buildings.Building',
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Корпус'
    )
    section = models.ForeignKey(
        to='buildings.Section',
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Секция/подъезд'
    )
    floor = models.ForeignKey(
        to='buildings.Floor',
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='Этаж'
    )
    number = models.IntegerField(verbose_name='Номер')
    area = models.DecimalField(verbose_name='Местоположение', decimal_places=2)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2)
    # TODO Property status choices
    status = models.CharField(
        choices=PROPERTY_STATUS_CHOICES,
        max_length=64,
        verbose_name='Статус'
    )
    # TODO Property type choices
    type = models.CharField(
        choices=PROPERTY_TYPE_CHOICES,
        max_length=64,
        verbose_name='Тип помещения'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Объект собственности'
        verbose_name_plural = 'Объекты собственности'
