
from django.urls import path
from app_entrega1.views import fecha, autores, formulario_autores


urlpatterns = [
    path('', fecha),
    path('autores/', autores, name = "Autores"),
    path('autoresFormulario/', formulario_autores, name = "Formulario_Autores")
]
