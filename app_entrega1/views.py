from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from datetime import datetime
from app_entrega1.models import Autores
#from app_entrega1.forms import AutorFormulario

# Create your views here.


def fecha(request):
    today = datetime.now()
    dict_context = {"today":today}
    return render(request,"app_entrega1/posts.html", dict_context)

def autores(request):
    autores = Autores.objects.filter(apellido="King")
    return render(request,"app_entrega1/autores.html")

def formulario_autores(request):
    return render(request,"app_entrega1/autoresFormulario.html")    
