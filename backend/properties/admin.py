from django.contrib import admin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Объект недвижимости"""

    list_display = (
        'project',
        'building',
        'section',
        'floor',
        'number',
        'area',
        'price',
        'status',
        'type'
    )
    search_fields = ('id', 'number')
    list_filter = (
        ('project', RelatedDropdownFilter),
        ('building', RelatedDropdownFilter),
        ('section', RelatedDropdownFilter),
        ('floor', RelatedDropdownFilter)
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'project',
            'building',
            'section',
            'floor'
        )