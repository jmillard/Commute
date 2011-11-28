from django.forms import ModelForm
from citzincident.models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
    
