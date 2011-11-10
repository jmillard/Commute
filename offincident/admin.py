from offincident.models import Official, Cause, IncidentType
from django.contrib import admin

class IncidentTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"incident_type_slug": ("incident_type",)}

admin.site.register(Official)
admin.site.register(Cause)
admin.site.register(IncidentType, IncidentTypeAdmin)

