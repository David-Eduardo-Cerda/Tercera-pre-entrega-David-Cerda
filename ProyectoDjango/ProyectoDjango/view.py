from django.http import HttpRequest , HttpResponse
from django.template import Template, Context
from django.template import loader

def ProbandoTemplate(request):
    
    diccionario = {"nombre" : "david" , "apellido" : "cerda", "edad" : 33}


    archivo = open("C:/Users/David/Desktop/Tercera-pre-entrega-David-Cerda/ProyectoDjango/Plantilla/template1.html")


    template = Template(archivo.read())
    archivo.close()
    contexto = Context(diccionario)

    documento = template.render(contexto)

    return HttpResponse(documento)