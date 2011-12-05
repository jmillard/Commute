from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'commute.offincident.views.homepage', name='home'),
    url(r'^citizen-reports/$', 'commute.citzincident.views.citizen_reports', name='citizen_reports'),
    url(r'^citizen-reports/(?P<incident_type>[-\w]+)/$', 'commute.citzincident.views.citizen_reports_details'), 
    url(r'^official-reports/$', 'commute.offincident.views.official_reports', name='official_reports'), 
    url(r'^official-reports/(?P<incident_type>[-\w]+)/$', 'commute.offincident.views.official_reports_details'), 
    url(r'^latest-reports/$', 'commute.offincident.views.latest_reports', name='incident_type'), 
    url(r'^latest-reports/(?P<location>[-\w]+)/$', 'commute.offincident.views.latest_reports_details'),
    url(r'^report-add/$', 'commute.citzincident.views.report_add'),
    url(r'^search/$', 'commute.offincident.views.search'),
    url(r'^search-details/$', 'commute.offincident.views.search_details'),

    # url(r'^commute/', include('commute.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
