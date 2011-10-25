from django.db import models
from locations.models import Location
from offincident.models import Cause
from offincident.models import IncidentType

class Report(models.Model):
    incident_type = models.ForeignKey(IncidentType)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    cause = models.ForeignKey(Cause)
    def __unicode__(self):
        return self.report

