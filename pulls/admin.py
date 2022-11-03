from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import Employee, Service, nous_contacter #import the Person model


# Register your models here.

admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(nous_contacter)


