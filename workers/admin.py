from django.contrib import admin
from .models import Bank,Ifscode,Account,Designation,City,Company,Worker

# Register your models here.
admin.site.register(Bank)
admin.site.register(Ifscode)
admin.site.register(Account)
admin.site.register(Designation)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Worker)
