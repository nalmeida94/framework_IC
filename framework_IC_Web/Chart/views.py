from django.shortcuts import render, render_to_response;
from django.http import HttpResponse;
from Tag.models import Tag, TagInfo;
from Tag.form import TagForm, TagInfoForm;
from Values.models import Values;
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas;
from matplotlib.figure import Figure;
from matplotlib.dates import DateFormatter;


#CHART	############################################################################
def selection(request):
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		tagInfos = TagInfo.objects.filter(name__icontains = textToSearch)

		tagInfoIds = []
		for tagInfo in tagInfos:
			tagInfoIds.append(tagInfo.id)
		tags = Tag.objects.filter(tagInfo__id__in = tagInfoIds)

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
			'tagInfos' : TagInfo.objects.all(),
			'keyword' : None
			}
		)


def chart(request):
	if 'checks[]' in request.GET and request.GET['checks[]']:
		#getting id's of selected tags
		chosen = request.GET.getlist('checks[]')
		
		urlEnd=""
		if(len(chosen) > 0):
			urlEnd = "?checks%5B%5D="
		count = 0
		size = len(chosen)
		while count < size:			
			urlEnd = urlEnd+chosen[count]
			count = count + 1
			if count < size :
				urlEnd = urlEnd+"&checks%5B%5D="
		tags = Tag.objects.filter(id__in = chosen)


		"""
		dic = {}
		myTuple = ("datetime",)
		tagIds = [];
		for tag in tags:
			tagIds.append(tag.id)

		for tag in tags:
			#if there is values on this tag
			if Values.objects.filter(id = tag.id).count>0:
				aux = Values.objects.filter(id = tag.id)
				result = TagInfo.objects.get(id = tag.tagInfo.id)
				dic["value"] =  result.description
				myTuple = myTuple +("value",)
		#this verify is only to put the description on the graph

		values2 = Values.objects.filter(tag__in = tagIds)
		values = aux.order_by('-datetime').to_json(order=myTuple, labels=dic)
		
		return render_to_response('Chart/chart.html',
				{
				'chosen' : chosen,
				'tags' : tags,
				'values' : values,
				'values2' : values2,
				'tagIds' : tagIds
				}
			)
		"""
		return render_to_response('Chart/chart.html',
				{
				'tags' : tags,
				'chosen' : chosen,
				'urlEnd' : urlEnd,
				}
			)
	else:
		return render_to_response('Chart/chart.html',
				{

				}
			)


def chartLines(request):		
	if 'checks[]' in request.GET and request.GET['checks[]']:
		#getting id's of selected tags
		chosen = request.GET.getlist('checks[]')
		tags = Tag.objects.filter(id__in = chosen)
		fig=Figure()
		ax=fig.add_subplot(111)
		strIdTags = ""
		#getting all values of all selected tags
		for tag in tags:
			if Values.objects.filter(tag = tag.id).count > 0:
				#values of one tag
				values = Values.objects.filter(tag = tag.id)
				strIdTags+=str(tag.id)
				strIdTags+="; "
				x = []
				y = []
				#all values of one tag
				for value in values:
					y.append(value.value)
					x.append(value.datetime)
					#ax.plot_date(value.value, value.datetime, '-')
				ax.plot_date( x, y, '-' , label = "Tag "+str(tag.id))
				#ax.set_ylabel("asdddddddddddddddddddddddddd")
				#ax.annotate("Tag "+str(tag.id), (x[0],y[0]), arrowprops=dict(facecolor='black', shrink=0.05))
		ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y - %H:%M:%S'))

		strIdTags = strIdTags[0:-2]
		ax.set_title("Values of Tags: "+strIdTags)
		ax.set_xlabel("Date-Time")
		ax.set_ylabel("Values")

		ax.legend(loc="upper right")
		fig.autofmt_xdate()
		canvas=FigureCanvas(fig)
		response=HttpResponse(content_type='image/png')
		#response=HttpResponse("<h1>Page not found</h1> content_type=%s" % 'image/png')
		canvas.print_png(response)
		return response
	else:
		response=HttpResponse("None value to make the chart")
		return response

"""
def chart(request):	
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter
	if 'checks[]' in request.GET and request.GET['checks[]']:
		#getting id's of selected tags
		chosen = request.GET.getlist('checks[]')
		tags = Tag.objects.filter(id__in = chosen)
		tagIds = [];
		for tag in tags:
			tagIds.append(tag.id)
		values = Values.objects.filter(tag__in = tagIds)
		fig=Figure()
		ax=fig.add_subplot(111)
		y=[]
		x=[]		
		for value in values:
			y.append(value.value)
			x.append(value.datetime)
			ax.plot_date(value.value, value.datetime, '-')	
		#ax.plot_date(x, y, '-')
		ax.xaxis.set_major_formatter(DateFormatter('%d-%m-%Y'))
		fig.autofmt_xdate()
		canvas=FigureCanvas(fig)
		response=HttpResponse(content_type='image/png')
		canvas.print_png(response)
		return response
"""
	    

def chartPie(request, tag_info_id):
	"""
	import random
	num_signed_off = random.randint(0, 10)
	num_reviewed = random.randint(0, 50)
	num_unreviewed = random.randint(0, 50)

	fig = Figure()
	ax = fig.add_subplot(111, aspect='equal')
	ax.pie([num_signed_off, num_reviewed, num_unreviewed],
            labels=['Signed Off', 'Reviewed', 'Unreviewed'],
            )
	ax.set_title('My Overall Stats')
	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type="image/png")
	canvas.print_png(response)
	return response
	"""
	qtds = []
	labels = []
	tags = Tag.objects.filter(id = tag_info_id)
	for tag in tags:
		qtd = Values.objects.filter(tag = tag.id).count()
		qtds.append(str(qtd))
		labels.append("Tag "+str(tag.id))
	fig = Figure()
	ax = fig.add_subplot(111, aspect='equal')
	ax.pie(qtds, labels=labels,)
	ax.set_title('Tag info '+str(tag_info_id))
	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type="image/png")
	canvas.print_png(response)
	return response
