from django.contrib import admin
from .models import Machine, Address, Customer, ServiceEngineer, Part, ServiceLog

admin.site.register(Machine)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(ServiceEngineer)
admin.site.register(Part)
admin.site.register(ServiceLog)