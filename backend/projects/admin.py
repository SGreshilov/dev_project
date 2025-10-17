from django.contrib import admin

from .models import Project


# admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Проект ЖК"""

    list_display = (
        'name',
        'slug',
        'type',
    )
    search_fields = ('id', 'name')
