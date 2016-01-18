from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #TAGINFO URL
    url(r'^search/$', 'Tag.views.tagInfosSearch'),
    url(r'^get/(?P<tagInfo_id>\d+)/$', 'Tag.views.tagInfo'),
    url(r'^add/$', 'Tag.views.tagInfoEdit'),
    url(r'^edit/(?P<tagInfo_id>\d+)/$', 'Tag.views.tagInfoEdit'),
)
