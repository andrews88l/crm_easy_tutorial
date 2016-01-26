from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePage(TemplateView):
	"""
	Because our needs are so simple, all we have to do is assign one value; template_name. The home.html file will be created in the next lesson.
	"""
	template_name = 'marketing/home.html'