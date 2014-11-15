from django.contrib import admin
from .models import Machine, Address, Customer, ServiceEngineer, ServiceLog

admin.site.register(Machine)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(ServiceEngineer)
admin.site.register(ServiceLog)