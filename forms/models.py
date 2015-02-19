from django.contrib.auth.models import User
from django.db import models

class Form(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Element(models.Model):
    form = models.ForeignKey(Form)
    ELEMENT_CHOICES = (
        ('BO', 'Boolean'),
        ('IN', 'Integer'),
    )
    type = models.CharField(max_length=20, choices=ELEMENT_CHOICES)
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name