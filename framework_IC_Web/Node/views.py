from django.shortcuts import render, render_to_response;
from django.http import HttpResponse;
from models import Node;
from Datasource.models import Datasource;
from form import NodeForm;

#NODES ###########################################################################
def nodesSearch(request):
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		return render_to_response('Node/nodes.html',
			{
			'nodes' : Node.objects.filter(name__icontains = request.GET['textToSearch']),
			'keyword' : request.GET['textToSearch']
			}
		)
	else:
		return render_to_response('Node/nodes.html',
			{
			'nodes' : Node.objects.all(),
			'keyword' : None
			}
		)

def node(request, node_id = 1):
	#if there is
	if Node.objects.filter(id=node_id).count()>0 :
		result = Node.objects.get(id=node_id)
		if Datasource.objects.filter(node__id = node_id).count()>0:
			datasources = Datasource.objects.filter(node__id = node_id)
		else:
			datasources = None
		return render_to_response('Node/node.html',
			{'node' : result , 'datasources' : datasources}
		)
	else:
		return render_to_response('Node/nodeDoesNotExist.html',
			{'node_id' : node_id }
		)

def nodeEdit(request, node_id=None):
    if node_id:
        node = Node.objects.get(id = node_id)
    else:
        node = None

    if request.method == 'POST':
        form = NodeForm(request.POST, instance=node)

        if form.is_valid():
            node = form.save()

            if node:
            	mensage = "You successfully saved the Node with id %s"%node_id
                return render_to_response('Node/nodes.html',
					{
					'nodes' : Node.objects.all(),
					'keyword' : None
					}
				)
    else:
        form = NodeForm(instance=node)

    return render(request, 'Node/nodeEdit.html',locals(),)
