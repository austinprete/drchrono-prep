from django.contrib import admin

from schedule.models import Doctor, PatientFamily, Patient


class PatientFamilyInlines(admin.TabularInline):
    model = PatientFamily
    extra = 3


class PatientInlines(admin.TabularInline):
    model = Patient
    extra = 2


class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatientFamilyInlines]


class PatientFamilyAdmin(admin.ModelAdmin):
    inlines = [PatientInlines]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(PatientFamily, PatientFamilyAdmin)
admin.site.register(Patient)