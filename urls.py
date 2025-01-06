from django.urls import path
from .views import (admins_list, create_admin, create_role, create_permission, create_role_permission, edit_admin,
                    edit_role, edit_permission, roles_list, permissions_list, role_permissions_list, delete_role,
                    delete_permission, delete_admin, delete_role_permission, activity_logs_list, view_activity_log,
                    main__, index)

app_name = 'admins'

urlpatterns = [
    path('', main__),
    path('create_admin/', create_admin, name='create_admin'),
    path('admins_list/', admins_list, name='admins_list'),
    path('edit_admin/<int:admin_id>/', edit_admin, name='edit_admin'),
    path('delete_admin/<int:admin_id>/', delete_admin, name='delete_admin'),
    path('create_role/', create_role, name='create_role'),
    path('roles_list/', roles_list, name='roles_list'),
    path('edit_role/<int:role_id>/', edit_role, name='edit_role'),
    path('delete_role/<int:role_id>/', delete_role, name='delete_role'),
    path('create_permission/', create_permission, name='create_permission'),
    path('permissions_list/', permissions_list, name='permissions_list'),
    path('edit_permission/<uuid:permission_id>/', edit_permission, name='edit_permission'),
    path('delete_permission/<uuid:permission_id>/', delete_permission, name='delete_permission'),
    path('create_role_permission/', create_role_permission, name='create_role_permission'),
    path('role_permissions_list/', role_permissions_list, name='role_permissions_list'),
    path('delete_role_permission/<int:role_permission_id>/', delete_role_permission, name='delete_role_permission'),
    path('activity_logs_list/', activity_logs_list, name='activity_logs_list'),
    path('view_activity_log/<uuid:log_id>/', view_activity_log, name='view_activity_log'),
]