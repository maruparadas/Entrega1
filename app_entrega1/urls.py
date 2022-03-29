
from django.urls import path
from app_entrega1.views import fecha, autores, formulario_autores, formulario_editorial, formulario_libros,buscar_libros,buscar


urlpatterns = [
    path('', fecha),
    path('autores/', autores, name = "Autores"),
    path('autoresFormulario/', formulario_autores, name = "Formulario_Autores"),
    path('editorialFormulario/', formulario_editorial, name = "Formulario_Editorial"),
    path('librosFormulario/', formulario_libros, name = "Formulario_Libros"),
    #urlsmaru
    path('librosBuscar/', buscar_libros, name = "Buscar_Libros"),
   # path('buscar/', buscar),
    ]
