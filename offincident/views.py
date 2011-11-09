from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response

def homepage(request):
    official = Official.objects.order_by('incident_type')
    location = Location.objects.order_by('location')
    return render_to_response('homepage.html', {
        'official':official,
        'location':location,
    })

def official_reports(request):
    official = Official.objects.order_by('incident_type')
    return render_to_response('official_reports.html', {
        'official':official,
    })

def official_reports_details(request, official_reports):
    official = Official.objects.filter('incident_type')
    return render_to_response('official_reports_details.html', {
        'official':official,
    })
