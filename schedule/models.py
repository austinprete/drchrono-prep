from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return ("%s, %s" % (self.last_name, self.first_name))


class PatientFamily(models.Model):
    doctor = models.ForeignKey(Doctor)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name


class Patient(models.Model):
    family = models.ForeignKey(PatientFamily)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)

    def __str__(self):
        return ("%s, %s" % (self.last_name, self.first_name))
