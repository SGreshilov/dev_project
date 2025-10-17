from django.contrib import admin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models.building import Building
from .models.floor import Floor
from .models.section import Section


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    """Корпус"""

    list_display = (
        'project',
        'number',
        'commission_date',
    )
    search_fields = ('id', 'number')
    list_filter = (
        ('project', RelatedDropdownFilter),
        # 'project',
        'commission_date',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('project')


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    """Этаж"""

    list_display = (
        'project',
        'building',
        'section',
        'number'
    )
    search_fields = ('id', 'number')
    list_filter = (
        ('project', RelatedDropdownFilter),
        ('building', RelatedDropdownFilter),
        ('section', RelatedDropdownFilter),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'project',
            'building',
            'section'
        )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """Секция/подъезд"""

    list_display = (
        'project',
        'building',
        'number',
        'floor_count',
    )
    search_fields = ('id', 'number')
    list_filter = (
        ('project', RelatedDropdownFilter),
        ('building', RelatedDropdownFilter),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('project', 'building')