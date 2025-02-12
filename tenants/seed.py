from .models import Tenant

def run():
    Tenant.objects.create(name="Empresa 1", is_active=True)
    Tenant.objects.create(name="Empresa 2", is_active=False)
    print("Seed data added.")