from .models import Tenant

def run():
    test_names = ["Empresa 1", "Empresa 2"]
    
    Tenant.objects.filter(name__in=test_names).delete()
    
    Tenant.objects.create(name="Empresa 1", is_active=True)
    Tenant.objects.create(name="Empresa 2", is_active=False)
    
    print("Seed data added.")