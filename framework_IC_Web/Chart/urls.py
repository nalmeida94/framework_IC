from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #CHART URL
    url(r'^selection/$', 'Chart.views.selection'),
    url(r'^chart/$', 'Chart.views.chart'),
    url(r'^chart/image/$', 'Chart.views.chartLines'),
	url(r'^chart/TagInfo/(?P<tag_info_id>\d+)$', 'Chart.views.chartPie'),
)
