from django.conf.urls import patterns, include, url;


urlpatterns = patterns('',
    #NODES URL
    url(r'^search/$', 'Node.views.nodesSearch'),
    url(r'^get/(?P<node_id>\d+)/$', 'Node.views.node'),
    url(r'^add/$', 'Node.views.nodeEdit'),
	url(r'^edit/(?P<node_id>\d+)/$', 'Node.views.nodeEdit'),
)
