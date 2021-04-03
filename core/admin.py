from django.contrib import admin
from django import forms

from .models import (
    Industry,
    EmployeeRange,
    City,
    State,
    Company,
    Department,
    Designation,
    Ifs,
    Bank,
    Level,
    Employee,
    Employer,
    Attendance,
    Statement,
    Booking,
    QrCode,
    Setting,
    Pricing,
    Verifier,
    Domain,
    Application,
)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Application._meta.fields]
    search_fields = ('name', 'phone', 'company_email')


class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class EmployeeRangeAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class IfsAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'bank']


class LevelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Level._meta.fields]


class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'phone', 'email', 'mail_verified', 'company',
                  'company_verified', 'net_monthly_salary', 'deleted_at',
                  'verified_salary', 'due_day', 'kyc', 'e_nach', 'is_verified', 'employee_id',
                  'joining_date', 'salary_day', 'service_status',
                  'credit_limit', 'bank_account_number', 'ifs', 'confirmed', 'user',
                  'salary_type', 'agreed_with_terms_and_conditions', 'daily_salary',
                  'balance', 'credited', 'debited', 'withdraw', 'work_days', 'work_timings',
                  'employer', 'beneficiary_id', 'is_beneficiary', 'check_location',
                  'wish_listing', 'mail_enabled', 'mail_bounced', 'mail_token',
                  'unsubscribe_token', 'digital_time_stamp']


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    model = Employee
    list_display = ['id', 'rid', 'name', 'phone', 'email', 'view_mail_verified', 'company',
                    'view_company_verified', 'net_monthly_salary',
                    'verified_salary', 'due_day', 'view_kyc', 'view_e_nach', 'view_is_verified',
                    'digital_time_stamp']
    search_fields = ('name', 'phone', 'email', 'is_verified')

    def view_is_verified(self, obj):
        if obj.is_verified == True:
            value = 'True'
        elif obj.is_verified == False:
            value = 'False'
        else:
            value = "Unknown"
        return value

    def view_e_nach(self, obj):
        if obj.e_nach == True:
            value = 'True'
        elif obj.e_nach == False:
            value = 'False'
        else:
            value = "Unknown"
        return value

    def view_company_verified(self, obj):
        if obj.company_verified == True:
            value = 'True'
        elif obj.company_verified == False:
            value = 'False'
        else:
            value = "Unknown"
        return value

    def view_kyc(self, obj):
        if obj.kyc == True:
            value = 'True'
        elif obj.kyc == False:
            value = 'False'
        else:
            value = "Unknown"
        return value

    def view_mail_verified(self, obj):
        if obj.mail_verified == True:
            value = 'True'
        elif obj.mail_verified == False:
            value = 'False'
        else:
            value = "Unknown"
        return value


class EmployerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employer._meta.fields]


class AttendanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Attendance._meta.fields]


class StatementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Statement._meta.fields]


class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]


class QrCodeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QrCode._meta.fields]


class SettingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Setting._meta.fields]


class PricingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pricing._meta.fields]


class VerifierAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Verifier._meta.fields]


class DomainAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Industry, IndustryAdmin)
admin.site.register(EmployeeRange, EmployeeRangeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Ifs, IfsAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Statement, StatementAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(QrCode, QrCodeAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Verifier, VerifierAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Application, ApplicationAdmin)
