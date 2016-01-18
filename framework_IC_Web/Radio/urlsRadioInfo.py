from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #RADIOTIPO URL
    url(r'^search/$', 'Radio.views.radioInfosSearch'),
    url(r'^get/(?P<radioInfo_id>\d+)/$', 'Radio.views.radioInfo'),
    url(r'^add/$', 'Radio.views.radioInfoEdit'),
    url(r'^edit/(?P<radioInfo_id>\d+)/$', 'Radio.views.radioInfoEdit'),
)
