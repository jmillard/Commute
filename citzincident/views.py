from commute.citzincident.models import Report
from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response

def citizen_reports(request):
    location = Location.objects.order_by('location')
    reports = Report.objects.order_by('incident_type')
    return render_to_response('citizen_reports.html', {
        'location':location,
        'reports':reports,
    })

def citizen_reports_details(request, incident_type):
    reports = IncidentType.objects.get(id=incident_type)
    return render_to_response('incident_type_details.html', {
        'incident_type':incident_type,
    })
