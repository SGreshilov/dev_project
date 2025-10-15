from django.db import models

from .constants import PropertyType, PropertyStatus


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
    area = models.DecimalField(
        verbose_name='Местоположение',
        decimal_places=2,
        max_digits=10
    )
    price = models.DecimalField(
        verbose_name='Цена',
        decimal_places=2,
        max_digits=20
    )
    status = models.IntegerField(
        choices=PropertyStatus.choices,
        verbose_name='Статус',
        default=PropertyStatus.ON_SALE
    )
    type = models.CharField(
        choices=PropertyType.choices,
        max_length=64,
        verbose_name='Тип помещения',
        default=PropertyType.FLAT
    )
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Объект собственности'
        verbose_name_plural = 'Объекты собственности'

    def __str__(self):
        return f'{self.project} - {self.building} - {self.section} - {self.floor} - {self.number}'