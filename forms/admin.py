from django.contrib import admin

# Register your models here.
from forms.models import Form, Element
admin.site.register(Form)
admin.site.register(Element)