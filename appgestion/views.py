from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def comges(request):
    return render(request,'comges.html')

def gestionclinica(request):
    return render(request,'gestionclinica.html')

def glosa(request):
    return render(request,'glosa.html')

def iaaps(request):
    return render(request,'iaaps.html')

def metasanitarias(request):
    return render(request,'metasanitarias.html')
