from django.shortcuts import render, redirect, get_object_or_404

from .forms import RoleForm, AdminsForm, ActivityForm, PermissionForm, RolePermissionForm
from .models import Role, AdminsMain, ActivityLog, RolePermission, Permission

from django.http import HttpResponse


def create_admin(request):
    if request.method == 'POST':
        form = AdminsForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.set_password(form.cleaned_data['password_hash'])  # Хэшируем пароль
            admin.save()
            return redirect('admins_list')
    else:
        form = AdminsForm()

    return render(request, 'create_admin.html', {'form': form})


def admins_list(request):
    admins = AdminsMain.objects.all()
    return render(request, 'admins_list.html', {'admins': admins})


def edit_admin(request, admin_id):
    admin = get_object_or_404(AdminsMain, id=admin_id)
    if request.method == 'POST':
        form = AdminsForm(request.POST, instance=admin)
        if form.is_valid():
            admin = form.save(commit=False)
            if 'password_hash' in form.cleaned_data:  # Хэшируем пароль, если он изменён
                admin.set_password(form.cleaned_data['password_hash'])
            admin.save()
            return redirect('admins_list')
    else:
        form = AdminsForm(instance=admin)

    return render(request, 'edit_admin.html', {'form': form})


def delete_admin(request, admin_id):
    admin = get_object_or_404(AdminsMain, id=admin_id)
    admin.delete()
    return redirect('admins_list')


def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу данных
            return redirect('role_list')  # Перенаправление на список ролей
    else:
        form = RoleForm()  # Пустая форма для GET-запроса

    return render(request, 'create_role.html', {'form': form})


def roles_list(request):
    roles = Role.objects.all()
    return render(request, 'roles_list.html', {'roles': roles})


def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roles_list')
    else:
        form = RoleForm(instance=role)

    return render(request, 'edit_role.html', {'form': form})


def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.delete()
    return redirect('roles_list')


def create_permission(request):
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('permissions_list')
    else:
        form = PermissionForm()

    return render(request, 'create_permission.html', {'form': form})


def permissions_list(request):
    permissions = Permission.objects.all()
    return render(request, 'permissions_list.html', {'permissions': permissions})


def edit_permission(request, permission_id):
    permission = get_object_or_404(Permission, id=permission_id)
    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permission)
        if form.is_valid():
            form.save()
            return redirect('permissions_list')
    else:
        form = PermissionForm(instance=permission)

    return render(request, 'edit_permission.html', {'form': form})


def delete_permission(request, permission_id):
    permission = get_object_or_404(Permission, id=permission_id)
    permission.delete()
    return redirect('permissions_list')


def create_role_permission(request):
    if request.method == 'POST':
        form = RolePermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_permissions_list')
    else:
        form = RolePermissionForm()

    return render(request, 'create_role_permission.html', {'form': form})


def role_permissions_list(request):
    role_permissions = RolePermission.objects.all()
    return render(request, 'role_permissions_list.html', {'role_permissions': role_permissions})


def delete_role_permission(request, role_permission_id):
    role_permission = get_object_or_404(RolePermission, id=role_permission_id)
    role_permission.delete()
    return redirect('role_permissions_list')


def activity_logs_list(request):
    logs = ActivityLog.objects.all()
    return render(request, 'activity_logs_list.html', {'logs': logs})


def view_activity_log(request, log_id):
    log = get_object_or_404(ActivityLog, id=log_id)
    return render(request, 'view_activity_log.html', {'log': log})


def index(request):
    return HttpResponse("<h1>HELLO<h1/>")


def main(request):
    return HttpResponse("<h1>NEW MAIN PAGE<h1/>")
