from commute.citzincident.models import Report
from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response

def report(request):
    report = Report.objects.order_by('incident_type')
    return render_to_response('report.html', {
        'report':report,
    })
