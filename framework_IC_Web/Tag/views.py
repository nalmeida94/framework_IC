from django.shortcuts import render, render_to_response;
from django.http import HttpResponse;
from models import Tag, TagInfo;
from form import TagForm, TagInfoForm;
from Values.models import Values;

import csv;


#TAG	############################################################################
def tagsSearch(request):
	#if 'textToSearch' in request.GET:
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		tagInfos = TagInfo.objects.filter(name__icontains = textToSearch)

		tagInfoIds = []
		for tagInfo in tagInfos:
			tagInfoIds.append(tagInfo.id)
		tags = Tag.objects.filter(tagInfo__id__in = tagInfoIds)

		return render_to_response('Tag/tags.html',
			{
			#'tags' : Tag.objects.filter(taginfo_idtaginfo1__idtaginfo = idtaginfo),
			'tags' : tags,
			'tagInfos' : tagInfos,
			'keyword' : textToSearch
			}
		)
	else:
		return render_to_response('Tag/tags.html',
			{
			'tags' : Tag.objects.all(),
			'tagInfos' : TagInfo.objects.all(),
			'keyword' : None
			}
		)

def tag(request, tag_id = 1):
	# if there is
	if Tag.objects.filter(id = tag_id).count()>0 :
		result = Tag.objects.get(id = tag_id)

		hasInfo = False
		tagInfo = None
		#if there is information about this tag
		if TagInfo.objects.filter(id = result.tagInfo.id).count() > 0:
			tagInfo = TagInfo.objects.get(id = result.tagInfo.id)
			hasInfo = True
		#if there is values on this tag
		if Values.objects.filter(tag = tag_id).count>0:
			aux = Values.objects.filter(tag = tag_id)
			'''
			#this verify is only to put the description on the graph
			if hasInfo:
				aux = aux.values("datahora").annotate(Sum("valor")).order_by()
				values = aux.order_by('-datahora').to_json(order=("datahora", "valor__sum"),
                                                        labels={"valor__sum": tagInfo.descricao})
			'''


			dic = {}
			myTuple = ("datetime",)

			dic["value"] =  tagInfo.description
			myTuple = myTuple +("value",)

			#this verify is only to put the description on the graph
			values = aux.order_by('-datetime').to_json(order=myTuple,
		                                                        labels=dic)

		else:
			values = None
		return render_to_response('Tag/tag.html',
			{'tag' : result, 'values' : values, 'tagInfo' : tagInfo}
		)
	else:
		return render_to_response('Tag/tagDoesNotExist.html',
			{'tag_id' : tag_id }
		)

def tagEdit(request, tag_id = None):
	if tag_id:
		tag = Tag.objects.get(id = tag_id)
	else:
		tag = None

	if request.method == 'POST':
		form = TagForm(request.POST, instance = tag)

		if form.is_valid():
			tag = form.save()

			if tag:
				return render_to_response('Tag/tags.html',
					{
					'tags' : Tag.objects.all(),
					'tagInfos' : TagInfo.objects.all(),
					'keyword' : None
					}
				)
	else:
		form = TagForm(instance = tag)

	return render(request, 'Tag/tagEdit.html',locals(),)

def tagGetValues(request, tag_id = 1):
	# if there is
	if Tag.objects.filter(id = tag_id).count()>0 :

		#if there is values on this tag
		if Values.objects.filter(tag_id = tag_id).count>0:
			values = Values.objects.filter(tag_id = tag_id)

			# Create the HttpResponse object with the appropriate CSV header.
			response = HttpResponse(content_type='text/csv')
		    #'Values of - tag %s - %s' %s (tag_id, date.today())
			response['Content-Disposition'] = 'attachment; filename=Values tag-ID %s.csv' % tag_id;

			writer = csv.writer(response);
			writer.writerow(['Tag; %s' % tag_id]);
			writer.writerow(['Date - time; Value']);

			for value in values:
				writer.writerow(["%s ; %s" % (value.datetime, value.value)]);

			return response;

		else:
			values = None;

			response = HttpResponse(content_type='text/csv');
		    #'Values of - tag %s - %s' %s (tag_id, date.today())
			response['Content-Disposition'] = 'attachment; filename=Values tag-ID %s.csv' % tag_id;
			writer = csv.writer(response);
			writer.writerow(['Tag; %s' % tag_id ]);
			writer.writerow(['Date - time; Value']);
			writer.writerow(['None value of this Tag.;None value of this Tag.']);
			return response;
	else:
		return render_to_response('Tag/tagDoesNotExist.html',
			{'tag_id' : tag_id }
		)
'''
def tagGetValuesPDF(request, tag_id = 1):
	# if there is
	if Tag.objects.filter(id = tag_id).count()>0 :

		#if there is values on this tag
		if Values.objects.filter(tag_id = tag_id).count>0:
			values = Values.objects.filter(tag_id = tag_id)

			# Create the HttpResponse object with the appropriate CSV header.
			response = HttpResponse(content_type='application/pdf')
		    #'Values of - tag %s - %s' %s (tag_id, date.today())
			response['Content-Disposition'] = 'attachment; filename=Values tag-ID %s.pdf' % tag_id;
			p = canvas.Canvas(response);
			p.drawString(3*inch, -3*inch, 'Tag',"                                     "+tag_id );
			p.drawString(1, 1, 'Date - time','                     Value');
			for value in values:				
				p.drawString(1, 1, [value.datetime, "     %s" % value.value]);
			p.showPage();
			p.save();
			return response;


		else:
			# Create the HttpResponse object with the appropriate CSV header.
			response = HttpResponse(content_type='application/pdf')
		    #'Values of - tag %s - %s' %s (tag_id, date.today())
			response['Content-Disposition'] = 'attachment; filename=Values tag-ID %s.pdf' % tag_id;
			p = canvas.Canvas(response);
			p.drawString(1, 1, 'Tag',"                                     "+tag_id );
			p.drawString(1, 1, 'Date - time','                     Value');
			p.drawString(1, 1, 'None value of this Tag.');
			p.showPage();
			p.save();
			return response;
	else:
		return render_to_response('Tag/tagDoesNotExist.html',
			{'tag_id' : tag_id }
		)
'''

#TAGINFO	############################################################################
def tagInfosSearch(request):
	#if 'textToSearch' in request.GET:
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		tagInfo = TagInfo.objects.filter(name__icontains = textToSearch)
		return render_to_response('TagInfo/tagInfos.html',
			{
			'tagInfos' : tagInfo,
			'keyword' : textToSearch
			}
		)
	else:
		return render_to_response('TagInfo/tagInfos.html',
			{
			'tagInfos' : TagInfo.objects.all(),
			'keyword' : None
			}
		)

def tagInfo(request, tagInfo_id = 1):
	# if there is
	if TagInfo.objects.filter(id = tagInfo_id).count()>0 :
		result = TagInfo.objects.get(id = tagInfo_id)

		tags = None
		#if there are tags of this type
		if Tag.objects.filter(tagInfo__id = result.id):
			tags = Tag.objects.filter(tagInfo__id = result.id)

		"""
		#LINE CHART
		dic = {}
		myTuple = ("datahora",)
		values = Tag.objects.none()
		for tag in tags:
			#if there is values on this tag
			if Valores.objects.filter(tag_idtag = tag.idtag).count>0:
				aux = Valores.objects.filter(tag_idtag = tag.idtag)
				values = values | aux
				dic["valor"] =  result.descricao
				myTuple = myTuple +("valor",)
		#aux = Valores.objects.filter(tag_idtag__in = tags)
		values = values.order_by('-datahora').to_json(order=myTuple,
	                                                        labels=dic)

		#PIECHART
		tagIds = []
		for tag in tags:
			tagIds.append(tag.idtag)
		qtdValuesTags = Valores.objects.filter(tag_idtag__in = tagIds)

		valuesPie = [['Tag','Amount of data']]
		#valuesPie = []
		for tag in tags:
			tagName = tag.taginfo_idtaginfo1.nome
			temp = [tagName.encode("ascii") , qtdValuesTags.filter(tag_idtag = tag.idtag).count()]
			#temp = [tag.taginfo_idtaginfo1.nome , qtdValuesTags.filter(tag_idtag = tag.idtag).count()]
			valuesPie.append(temp)


		valores = Valores.objects.filter(tag_idtag__in = tags)
		"""
		return render_to_response('TagInfo/tagInfo.html',
			{
			'tagInfo' : result,
			'tags' : tags,
			#'values' : values,
			#'valores' : valores,
			#'valuesPie' : valuesPie
			}
		)
	else:
		return render_to_response('TagInfo/tagInfoDoesNotExist.html',
			{'tagInfo_id' : tagInfo_id }
		)

def tagInfoEdit(request, tagInfo_id = None):
	if tagInfo_id:
		tagInfo = TagInfo.objects.get(id = tagInfo_id)
	else:
		tagInfo = None

	if request.method == 'POST':
		form = TagInfoForm(request.POST, instance = tagInfo)

		if form.is_valid():
			tagInfo = form.save()

			if tagInfo:
				return render_to_response('TagInfo/tagInfos.html',
					{
					'tagInfos' : TagInfo.objects.all(),
					'keyword' : None
					}
				)
	else:
		form = TagInfoForm(instance = tagInfo)

	return render(request, 'TagInfo/tagInfoEdit.html',locals(),)

"""
#CHART	############################################################################
def selection(request):
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		tagInfos = Taginfo.objects.filter(nome__icontains = textToSearch)

		tagInfoIds = []
		for tagInfo in tagInfos:
			tagInfoIds.append(tagInfo.idtaginfo)
		tags = Tag.objects.filter(taginfo_idtaginfo1__idtaginfo__in = tagInfoIds)

		return render_to_response('Chart/selection.html',
			{
			#'tags' : Tag.objects.filter(taginfo_idtaginfo1__idtaginfo = idtaginfo),
			'tags' : tags,
			'tagInfos' : tagInfos,
			'keyword' : textToSearch
			}
		)
	else:
		return render_to_response('Chart/selection.html',
			{
			'tags' : Tag.objects.all(),
			'tagInfos' : Taginfo.objects.all(),
			'keyword' : None
			}
		)


def chart(request):
	if 'checks[]' in request.GET and request.GET['checks[]']:
		#getting id's of selected tags
		chosen = request.GET.getlist('checks[]')

		tags = Tag.objects.filter(idtag__in = chosen)

		dic = {}
		myTuple = ("datahora",)

		for tag in tags:
			#if there is values on this tag
			if Valores.objects.filter(tag_idtag = tag.idtag).count>0:
				aux = Valores.objects.filter(tag_idtag = tag.idtag)
				result = Taginfo.objects.get(idtaginfo = tag.taginfo_idtaginfo1.idtaginfo)
				dic["valor"] =  result.descricao
				myTuple = myTuple +("valor",)
		#this verify is only to put the description on the graph
		values = aux.order_by('-datahora').to_json(order=myTuple,
	                                                        labels=dic)

		return render_to_response('Chart/chart.html',
				{
				'chosen' : chosen,
				'tags' : tags,
				'values' : values
				}
			)
	else:
		return render_to_response('Chart/chart.html',
				{

				}
			)

"""
