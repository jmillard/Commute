from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response

def homepage(request):
    official = Official.objects.order_by('-pub_date')
    location = Location.objects.order_by('location')
    incident_types = IncidentType.objects.order_by('incident_type')
    return render_to_response('homepage.html', {
        'official':official,
        'location':location,
        'incident_types': incident_types,
    })

def official_reports(request):
    official = Official.objects.order_by('incident_type')
    return render_to_response('official_reports.html', {
        'official':official,
    })

def official_reports_details(request, incident_type):
    official = Official.objects.get(id=incident_type)
    return render_to_response('official_reports_details.html', {
        'official':official,
    })

def incident_type(request):
    incident_type = IncidentType.objects.order_by('incident_type')
    return render_to_response('incident_type.html', {
        'incident_type':incident_type,
    })

def incident_type_details(request, location):
    incident_type = IncidentType.objects.get(id=incident_type)
    return render_to_response('incident_type_details.html', {
        'incident_type':incident_type,
    })
