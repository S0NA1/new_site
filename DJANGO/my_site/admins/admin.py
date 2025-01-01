from django.contrib import admin
from .models import AdminsMain, Role, Permission, ActivityLog, RolePermission

admin.site.register(AdminsMain)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermission)
admin.site.register(ActivityLog)
