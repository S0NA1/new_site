from django.contrib import admin
from .models import AdminsMain, Role, Permission, ActivityLog, RolePermission


@admin.register(AdminsMain)
class AdminsMainAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role_id', 'is_active')
    search_fields = ('username', 'email')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'role_description')
    search_fields = ('role_name',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'created_at')
    search_fields = ('user__username', 'action')


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    search_fields = ('role__role_name', 'permission__name')