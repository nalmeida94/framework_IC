from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #DATASOURCE URL
    url(r'^search/$', 'Datasource.views.datasourcesSearch'),
    url(r'^get/(?P<datasource_id>\d+)/$', 'Datasource.views.datasource'),
    url(r'^add/$', 'Datasource.views.datasourceEdit'),
    url(r'^edit/(?P<datasource_id>\d+)/$', 'Datasource.views.datasourceEdit'),
)
