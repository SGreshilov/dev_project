from django.db import models


class Floor(models.Model):
    """
    Модель этажа
    """
    project = models.ForeignKey(
        to='projects.Project',
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        to='Building',
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Корпус'
    )
    section = models.ForeignKey(
        to='Section',
        on_delete=models.CASCADE,
        related_name='floors',
        verbose_name='Секция/подъезд'
    )
    number = models.IntegerField(verbose_name='Номер')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'