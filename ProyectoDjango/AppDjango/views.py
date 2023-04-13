from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.template import Template, Context
from django.template import loader

def ProbandoTemplate(request):
    
    diccionario = {"nombre" : "david" , "apellido" : "cerda" , "lista" : [7,8,3,4,6]}


    template = loader.get_template('template1.html') #aca indico el nombre del temple y en settings senialo la ubicacion de la carpeta

    documento = template.render(diccionario)

    return HttpResponse(documento)
# Create your views here.
