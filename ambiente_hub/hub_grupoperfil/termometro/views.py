from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request,"termometro/index.html")


def atualizar(request):
   
    return render(request,"termometro/atualizar.html")