from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
	context_dict = {'boldmessage' : 'Crunchy, creamy,cookie'}
	return render(request,'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'name': 'yiern', 'MEDIA_URL': settings.MEDIA_URL}
	return render(request, 'rango/about.html',context=context_dict)
	return HttpResponse("Rango says here is the about page")

