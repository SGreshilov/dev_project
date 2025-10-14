from django.db import models

from .constants import PROJECT_TYPES_CHOICES


class Project(models.Model):
    """
    Модель ЖК
    """
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    type = models.CharField(max_length=64, choices=PROJECT_TYPES_CHOICES)