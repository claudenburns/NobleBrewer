from django.shortcuts import render
## removed infosite from request
def index(request):
    return render(request, 'infosite/index.html')

def about(request):
    return render(request, 'about.html')


