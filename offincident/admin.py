from offincident.models import Official, Cause, IncidentType
from django.contrib import admin

class IncidentTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"incident_type_slug": ("incident_type",)}

class CauseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"cause_slug": ("cause",)}

admin.site.register(Official)
admin.site.register(Cause, CauseAdmin)
admin.site.register(IncidentType, IncidentTypeAdmin)

