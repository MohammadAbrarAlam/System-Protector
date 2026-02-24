from django.contrib import admin
from .models import SystemStatus, Patch


@admin.register(SystemStatus)
class SystemStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpu', 'ram', 'disk', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('cpu', 'ram', 'disk')
    ordering = ('-created_at',)


@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'system_name', 'patch_version', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('system_name', 'patch_version', 'status')
    ordering = ('-date',)