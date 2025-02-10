from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse 
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm

def index(request):
	#queries category class from model and order them by likes, first 5 
	category_list = Category.objects.order_by('-likes')[:5] 
	pages_list = Page.objects.order_by('-views')[:5]

	context_dict = {'boldmessage' : 'Crunchy, creamy,cookie'}
	context_dict['categories'] = category_list
	context_dict['pages'] = pages_list
	return render(request,'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'name': 'yiern', 'MEDIA_URL': settings.MEDIA_URL}
	return render(request, 'rango/about.html',context=context_dict)
	return HttpResponse("Rango says here is the about page")


def show_category(request,category_name_slug):
	context_dict={}
	try:
		category = Category.objects.get(slug = category_name_slug)

		#Retrieve all related pages, the filter() will return a list of page objects 
		#under name pages
		pages = Page.objects.filter(category = category)

		context_dict['category'] = category
		context_dict['pages'] = pages
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None
	
	return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
	form = CategoryForm()

	# A HTTPS post?
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		# have we been provided with a valid form?
		if form.is_valid():
			# save new category into database
			form.save(commit = True)

			return redirect('/rango/')
		else:
			print(form.errors)

	return render(request, 'rango/add_category.html', {'form':form})

def add_page(request, category_name_slug):
	
	try:
		category = Category.objects.get(slug = category_name_slug)
	except Category.DoesNotExist:
		category = None
	
	if category is None:
		return redirect('/rango/')
	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)

		if form.is_valid():
			if category:
				page = form.save(commit = False)
				page.category = category
				page.views = 0
				page.save()

				return redirect(reverse('rango:show_category', kwargs={'category_name_slug':category_name_slug}))
			
			else:
				print(form.errors)

	context_dict = {'form': form, 'category': category}
	return render(request, 'rango/add_page.html', context= context_dict)
