from django.db import models


class Section(models.Model):
    """
    Модель секции/подъезда
    """
    project = models.ForeignKey(
        to='projects.Project',
        on_delete=models.CASCADE,
        related_name='sections',
        verbose_name='Проект ЖК'
    )
    building = models.ForeignKey(
        to='Building',
        on_delete=models.CASCADE,
        related_name='sections',
        verbose_name='Корпус'
    )
    number = models.CharField(max_length=64, verbose_name='Номер')
    floor_count = models.IntegerField(verbose_name='Количество этажей')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Секция/подъезд'
        verbose_name_plural = 'Секции/подъезды'

    def __str__(self):
        return f'{self.building} - {self.number}'