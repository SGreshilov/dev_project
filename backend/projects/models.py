from django.db import models

from .constants import PROJECT_TYPES_CHOICES


class Project(models.Model):
    """
    Модель проекта ЖК
    """
    name = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    # TODO Project type choices
    type = models.CharField(
        max_length=64, choices=PROJECT_TYPES_CHOICES, verbose_name='Тип')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Проект ЖК'
        verbose_name_plural = 'Проекты ЖК'
