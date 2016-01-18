from django.shortcuts import render, render_to_response;
from django.http import HttpResponse;
from models import Radio, RadioInfo;
from form import RadioForm, RadioInfoForm;

#RADIO	############################################################################
def radiosSearch(request):
	#if 'textToSearch' in request.GET:
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		radioInfo = RadioInfo.objects.filter(name__icontains = textToSearch)
		radio = Radio.objects.filter(radioInfo__id = radioInfo.id)
		return render_to_response('Radio/radios.html',
			{
			'radios' : radio,
			'radioInfos' : radioInfo,
			'keyword' : textToSearch
			}
		)
	else:
		return render_to_response('Radio/radios.html',
			{
			'radios' : Radio.objects.all(),
			'radioInfos' : RadioInfo.objects.all(),
			'keyword' : None
			}
		)

def radio(request, radio_id = 1):
	# if there is
	if Radio.objects.filter(id=radio_id).count()>0 :
		result = Radio.objects.get(id=radio_id)

		#if there is information about this Radio
		if RadioInfo.objects.filter(id = result.radioInfo.id).count() > 0:
			radioInfo = RadioInfo.objects.get(id = result.radioInfo.id)

		return render_to_response('Radio/radio.html',
			{'radio' : result, 'radioInfo' : radioInfo}
		)
	else:
		return render_to_response('Radio/radioDoesNotExist.html',
			{'radio_id' : radio_id }
		)

def radioEdit(request, radio_id = None):
    if radio_id:
        radio = Radio.objects.get(id=radio_id)
    else:
        radio = None

    if request.method == 'POST':
        form = RadioForm(request.POST, instance=radio)

        if form.is_valid():
            radio = form.save()

            if radio:
                return render_to_response('Radio/radios.html',
					{
					'radios' : Radio.objects.all(),
					'radioTipos' : RadioInfo.objects.all(),
					'keyword' : None
					}
				)

    else:
        form = RadioForm(instance = radio)

    return render(request, 'Radio/radioEdit.html',locals(),)

#RADIOTIPO	############################################################################
def radioInfosSearch(request):
	#if 'textToSearch' in request.GET:
	if 'textToSearch' in request.GET and request.GET['textToSearch']:
		textToSearch = request.GET['textToSearch']
		radioInfo = RadioInfo.objects.filter(name__icontains = textToSearch)
		return render_to_response('RadioInfo/radioTipos.html',
			{
			'radioInfos' : radioInfo,
			'keyword' : textToSearch
			}
		)
	else:
		return render_to_response('RadioInfo/radioTipos.html',
			{
			'radioInfos' : RadioInfo.objects.all(),
			'keyword' : None
			}
		)

def radioInfo(request, radioInfo_id = 1):
	# if there is
	if RadioInfo.objects.filter(id = radioInfo_id).count()>0 :
		result = RadioInfo.objects.get(id = radioInfo_id)

		radios = None
		if Radio.objects.filter(radioInfo_id = result.id):
			radios = Radio.objects.filter(radioInfo_id = result.id)
		return render_to_response('RadioInfo/radioTipo.html',
			{'radioInfo' : result, 'radios' : radios}
		)
	else:
		return render_to_response('RadioInfo/radioTipoDoesNotExist.html',
			{'radioInfo_id' : radioTipo_id }
		)

def radioInfoEdit(request, radioInfo_id = None):
	if radioInfo_id:
		radioInfo = RadioInfo.objects.get(id = radioInfo_id)
	else:
		radioInfo = None

	if request.method == 'POST':
		form = RadioInfoForm(request.POST, instance=radioTipo)

		if form.is_valid():
			radioInfo = form.save()

			if radioTipo:
				return render_to_response('RadioInfo/radioTipos.html',
					{
					'radioTipos' : RadioInfo.objects.all(),
					'keyword' : None
					}
				)
	else:
		form = RadioInfoForm(instance=radioInfo)

	return render(request, 'RadioInfo/radioTipoEdit.html',locals(),)
