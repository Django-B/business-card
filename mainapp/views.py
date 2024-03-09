from django.shortcuts import render

from .models import Setting, Category, Image

def index(request):
	categories = Category.objects.all()
	setting = Setting.objects.first()
	context = {
		'categories': categories,
		'setting': setting
	}
	return render(request, 'index.html', context=context)
