from django.shortcuts import render

def index(request):
    return render(request, 'infosite/index.html')

##from django.shortcuts import render_to_response
##def index(request):
##   return render_to_response('infosite/index.html')
