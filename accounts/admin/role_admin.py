from django.contrib import admin
from accounts.models import RoleModel

class RoleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_enabled', 'created', 'modified')
    list_filter = ('is_enabled',)
    search_fields = ('name', 'code', 'about')
    list_per_page = 20  # Opcional: Número de registros a mostrar por página en la vista de lista

    readonly_fields = ('created', 'modified')

admin.site.register(RoleModel, RoleModelAdmin)
