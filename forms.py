from django import forms
from .models import Role, ActivityLog, AdminsMain, Permission, RolePermission


class AdminsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdminsMain
        fields = ['username', 'email', 'password_hash', 'role_id', 'is_active']

    def save(self, commit=True):
        admin = super().save(commit=False)
        admin.set_password(self.cleaned_data['password'])  # Хэшируем пароль
        if commit:
            admin.save()
        return admin


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'role_description']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['user', 'action', 'details']


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name', 'description']


class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = RolePermission
        fields = ['role', 'permission']
