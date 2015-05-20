from django.shortcuts import render
import datetime

def home(request):
	now = datetime.datetime.now()
	return render(request, 'home.html', {'current_date': now})

def about(request):
	return render(request, 'about.html', {})
