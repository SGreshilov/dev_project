from django.db import models

from projects.models import Project


class Building(models.Model):
    """
    Модель корпуса
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='Проект ЖК')
    number = models.IntegerField(verbose_name='Номер')
    commission_date = models.DateField(verbose_name='Срок сдачи')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'