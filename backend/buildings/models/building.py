from django.db import models


class Building(models.Model):
    """
    Модель корпуса
    """
    project = models.ForeignKey(
        to='projects.Project',
        on_delete=models.CASCADE,
        verbose_name='Проект ЖК'
    )
    number = models.CharField(max_length=64, verbose_name='Номер')
    commission_date = models.DateField(verbose_name='Срок сдачи')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'