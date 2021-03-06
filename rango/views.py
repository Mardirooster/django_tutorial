from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
	context = RequestContext(request)


	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	for category in category_list:
		category.url = category.name.replace(' ','_')

	return render(request,'rango/index.html',context_dict,context)
# Create your views here.

def about(request):
	context = RequestContext(request)

	return render(request, 'rango/about.html')

def category(request, category_name_url):
	context = RequestContext(request)

	category_name=category_name_url.replace('_',' ')

	context_dict = {'category_name': category_name}

	try:
		category = Category.objects.get(name=category_name)

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages

		context_dict['category'] = category

	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict, context)

def add_category(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print(form.errors)
	else:
		form = CategoryForm()

	return render(request, 'rango/add_category.html', {'form': form}, context)