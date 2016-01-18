from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #RADIO URL
    url(r'^search/$', 'Radio.views.radiosSearch'),
    url(r'^get/(?P<radio_id>\d+)/$', 'Radio.views.radio'),
    url(r'^add/$', 'Radio.views.radioEdit'),
    url(r'^edit/(?P<radio_id>\d+)/$', 'Radio.views.radioEdit'),
)
