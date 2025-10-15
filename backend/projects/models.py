from django.db import models


class Project(models.Model):
    """
    Модель проекта ЖК
    """
    name = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    type = models.CharField(max_length=64, verbose_name='Тип')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Проект ЖК'
        verbose_name_plural = 'Проекты ЖК'

    def __str__(self):
        return self.name