from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'commute.offincident.views.homepage', name='home'),
    url(r'^report/$', 'commute.citzincident.views.report', name='report'),
    url(r'^official-reports/$', 'commute.offincident.views.official_reports', name='official_reports'), 
    url(r'^official-reports/(?P<incident_type>[-\w]+)/$', 'commute.offincident.views.official_reports_details'),  
# url(r'^commute/', include('commute.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
