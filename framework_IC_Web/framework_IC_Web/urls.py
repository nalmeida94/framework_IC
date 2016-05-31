from django.conf.urls import patterns, include, url;
from django.conf import settings
from django.contrib import admin;


urlpatterns = patterns('',
    url(r'^$', 'framework_IC_Web.views.home', name='home'),
    (r'^static/(?P<path>.*)$','django.views.static.server', {'document_root':settings.STATIC_ROOT}),
	(r'^media/(?P<path>.*)$','django.views.static.server', {'document_root':settings.MEDIA_ROOT}),

    url(r'^datasources/', include('Datasource.urls')),
    url(r'^nodes/', include('Node.urls')),
    url(r'^radioTipos/', include('Radio.urlsRadioInfo')),
    url(r'^radios/', include('Radio.urls')),
    url(r'^snapshots/', include('Snapshot.urls')),
    url(r'^tagInfos/', include('Tag.urlsTagInfo')),
    url(r'^tags/', include('Tag.urls')),
    url(r'^values/', include('Values.urls')),
    url(r'^chart/', include('Chart.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
