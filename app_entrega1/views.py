from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from datetime import datetime
from app_entrega1.models import Autores, Editorial, Libros
from app_entrega1.forms import AutorFormulario, EditorialFormulario, LibrosFormulario

# Create your views here.


def fecha(request):
    today = datetime.now()
    dict_context = {"today":today}
    return render(request,"app_entrega1/posts.html", dict_context)

def autores(request):
    return render(request,"app_entrega1/autores.html")

def formulario_autores(request):
    
    if request.method == 'POST':

        miFormulario = AutorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            autor = Autores(data['nombre'],data['apellido'])
    
            autor.save()

        return render(request,"app_entrega1/autoresFormulario.html") 

    else:

        miFormulario = AutorFormulario()

    return render(request,"app_entrega1/autoresFormulario.html",{"miFormulario":miFormulario})    

def formulario_editorial(request):
    
    if request.method == 'POST':

        miFormulario = EditorialFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            editorial = Editorial(data['nombre'],data['web'],data['pais_origen'])
    
            editorial.save()

        return render(request,"app_entrega1/editorialFormulario.html") 

    else:

        miFormulario = EditorialFormulario()

    return render(request,"app_entrega1/editorialFormulario.html",{"miFormulario":miFormulario})    

def formulario_libros(request):
    
    if request.method == 'POST':

        miFormulario = LibrosFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            libros = Libros(data['isbn'],data['idioma'],data['titulo'],data['fecha_publicacion'],data['clasificacion'])
    
            libros.save()

        return render(request,"app_entrega1/librosFormulario.html") 

    else:

        miFormulario = LibrosFormulario()

    return render(request,"app_entrega1/librosFormulario.html",{"miFormulario":miFormulario})    
