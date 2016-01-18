from django.shortcuts import render, render_to_response;
from django.http import HttpResponse;
from models import Datasource;
from Tag.models import Tag, TagInfo;
from form import DatasourceForm;

#DATASOURCE	############################################################################
def datasourcesSearch(request):
	#if 'textToSearch' in request.GET:
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		return render_to_response('Datasource/datasources.html',
			{
			'datasources' : Datasource.objects.filter(name__icontains = request.GET['textToSearch']),
			'keyword' : request.GET['textToSearch']
			}
		)
	else:
		return render_to_response('Datasource/datasources.html',
			{
			'datasources' : Datasource.objects.all(),
			'keyword' : None
			}
		)

def datasource(request, datasource_id = 1):
	# if there is
	if Datasource.objects.filter(id=datasource_id).count()>0 :
		result = Datasource.objects.get(id=datasource_id)
		#if there is tags on this datasource
		tags = None
		tagsInfos = None
		if Tag.objects.filter(datasource = datasource_id).count>0:
			tags = Tag.objects.filter(datasource = datasource_id)
			'''
			tagInfos = Taginfo.objects.all()
			'''
			tagInfoIds = []
			for tag in tags:
				tagInfoId = TagInfo.objects.get(id = tag.tagInfo.id)
				tagInfoIds.append(tagInfoId.id)
			tagInfos = TagInfo.objects.filter(id__in = tagInfoIds)
		else:
			tags = None
			tagsInfos = None
		return render_to_response('Datasource/datasource.html',
			#{'datasource' : result, 'tags' : tags}
			{'datasource' : result, 'tags' : tags, 'tagInfos' : tagInfos}
		)
	else:
		return render_to_response('Datasource/datasourceDoesNotExist.html',
			{'datasource_id' : datasource_id }
		)

def datasourceEdit(request, datasource_id=None):
    if datasource_id:
        datasource = Datasource.objects.get(id=datasource_id)
    else:
        datasource = None

    if request.method == 'POST':
        form = DatasourceForm(request.POST, instance=datasource)

        if form.is_valid():
            datasource = form.save()

            if datasource:
                return render_to_response('Datasource/datasources.html',
					{
					'datasources' : Datasource.objects.all(),
					'keyword' : None
					}
				)
    else:
        form = DatasourceForm(instance=datasource)

    return render(request, 'Datasource/datasourceEdit.html',locals(),)
