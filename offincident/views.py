from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response

def homepage(request):
    official = Official.objects.order_by('incident_type')
    location = Location.objects.order_by('zipcode')
    return render_to_response('homepage.html', {
        'official':official,
        'location':location,
    })
