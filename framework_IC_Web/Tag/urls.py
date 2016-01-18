from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #TAG URL
    url(r'^search/$', 'Tag.views.tagsSearch'),
    url(r'^get/(?P<tag_id>\d+)/$', 'Tag.views.tag'),
    url(r'^add/$', 'Tag.views.tagEdit'),
    url(r'^edit/(?P<tag_id>\d+)/$', 'Tag.views.tagEdit'),
    url(r'^getValues/(?P<tag_id>\d+)/$', 'Tag.views.tagGetValues'),
)
