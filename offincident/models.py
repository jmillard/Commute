from django.db import models
from locations.models import Location

class Cause(models.Model):
    cause = models.CharField(max_length=255)
    cause_slug = models.SlugField()
    def __unicode__(self):
        return self.cause

class IncidentType(models.Model):
    incident_type = models.CharField(max_length=255)
    incident_type_slug = models.SlugField()
    def get_absolute_url(self):
        return "/incident-type/%s/" % self.incident_type_slug
    def __unicode__(self):
        return self.incident_type

class Official(models.Model):
    incident_type = models.ForeignKey(IncidentType)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    cause = models.ForeignKey(Cause)
    def get_absolute_url(self):
        return "/official-reports/%i/" % self.id
    def __unicode__(self):
        return self.incident_type.incident_type
