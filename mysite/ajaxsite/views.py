from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
	return render(request, "dashboard.html")

def data(request):
	html=render_to_string('charts/data.html', {'name': 'John'})
	return HttpResponse(html)
