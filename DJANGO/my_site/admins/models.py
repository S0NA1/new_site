import uuid
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class AdminsMain(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.username


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=100, unique=True, db_index=True)
    role_description = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.role_name


class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_index=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, db_index=True)

    class Meta:
        unique_together = ('role', 'permission')

    def __str__(self):
        return f"{self.role.name} - {self.permission.name}"


class ActivityLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(AdminsMain, on_delete=models.CASCADE, related_name='activity_logs', db_index=True)
    action = models.CharField(max_length=100, db_index=True)
    details = models.JSONField(blank=True, null=True)  # PostgreSQL поддерживает JSONField
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"
