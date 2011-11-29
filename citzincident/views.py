from commute.citzincident.models import Report
from commute.offincident.models import Official, Cause, IncidentType
from commute.locations.models import Location
from django.shortcuts import render_to_response
from commute.citzincident.forms import ReportForm
from django.template import RequestContext

def citizen_reports(request):
    location = Location.objects.order_by('location')
    reports = Report.objects.order_by('incident_type')
    return render_to_response('citizen_reports.html', {
        'location':location,
        'reports':reports,
    })

def citizen_reports_details(request, incident_type):
    reports = Report.objects.get(id=incident_type)
    return render_to_response('citizen_reports_details.html', {
        'reports':reports,
    })

def report_add(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(citizen_report)
    return render_to_response('report_add.html', {'report_form': form, },  
                                context_instance = RequestContext(request))
