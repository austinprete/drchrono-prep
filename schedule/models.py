from django.db import models
from django.contrib.auth.models import User


class PatientFamily(models.Model):
    user = models.ForeignKey(User)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name


class Patient(models.Model):
    family = models.ForeignKey(PatientFamily)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Schedule(models.Model):
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.patient.first_name + "'s Schedule"


class Vaccine(models.Model):
    schedule = models.ForeignKey(Schedule)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Dose(models.Model):
    vaccine = models.ForeignKey(Vaccine)
    name = models.CharField(max_length=60)
    given = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.vaccine.schedule.patient.first_name} {self.vaccine.schedule.patient.last_name} - {self.name}'
