from django.contrib import admin

from .models.building import Building
from .models.floor import Floor
from .models.section import Section


admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Section)
