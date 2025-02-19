from django.db import models

class TenantManager(models.Manager):
    def get_by_id(self, tenant_id):
        return self.filter(id=tenant_id).first()

    def get_by_name(self, name):
        return self.filter(name=name).first()

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TenantManager()

    def __str__(self):
        return self.name