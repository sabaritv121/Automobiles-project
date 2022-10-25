from django.contrib import admin

# Register your models here.
from auto_app import models

admin.site.register(models.Worksmanager)
admin.site.register(models.Customer)
admin.site.register(models.Request)
admin.site.register(models.Complaints)
admin.site.register(models.Appointment)