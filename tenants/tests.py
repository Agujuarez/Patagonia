from django.test import TestCase
from .models import Tenant

class TenantManagerTest(TestCase):
    def setUp(self):
        self.tenant1 = Tenant.objects.create(name="Test Tenant 1", is_active=True)
        self.tenant2 = Tenant.objects.create(name="Test Tenant 2", is_active=False)

    def test_get_by_id(self):
        tenant = Tenant.objects.get_by_id(self.tenant1.id)
        self.assertEqual(tenant, self.tenant1)

        tenant_none = Tenant.objects.get_by_id(999)
        self.assertIsNone(tenant_none)

    def test_get_by_name(self):
        tenant = Tenant.objects.get_by_name("Test Tenant 2")
        self.assertEqual(tenant, self.tenant2)

        tenant_none = Tenant.objects.get_by_name("Not Exist")
        self.assertIsNone(tenant_none)