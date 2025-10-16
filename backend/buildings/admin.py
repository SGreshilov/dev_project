from django.contrib import admin

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models.building import Building
from .models.floor import Floor
from .models.section import Section


admin.site.register(Floor)
admin.site.register(Section)

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    """Корпус"""

    list_display = (
        '__str__',
        'number',
        'project',
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
