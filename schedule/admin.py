from django.contrib import admin

from schedule.models import PatientFamily, Patient, Schedule, Vaccine, Dose


class PatientFamilyInlines(admin.TabularInline):
    model = PatientFamily
    extra = 3


class PatientInlines(admin.TabularInline):
    model = Patient
    extra = 2


class PatientFamilyAdmin(admin.ModelAdmin):
    inlines = [PatientInlines]

admin.site.register(PatientFamily, PatientFamilyAdmin)
admin.site.register(Patient)
admin.site.register(Schedule)
admin.site.register(Vaccine)
admin.site.register(Dose)