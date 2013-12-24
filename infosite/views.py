from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'infosite/index.html')

#def about(request):
#    return render(request, 'infosite/about.html')

def about(request):
    return render(request, 'infosite/about.html')

#class AboutView(TemplateView):
#	template_name="about.html"

