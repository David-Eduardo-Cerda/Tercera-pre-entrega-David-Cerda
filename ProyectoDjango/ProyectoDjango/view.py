from django.http import HttpRequest , HttpResponse
from django.template import Template, Context
from django.template import loader

def ProbandoTemplate(request):
    
    diccionario = {"nombre" : "david" , "apellido" : "cerda", "edad" : 33, "lista" : [7,8,3,4,6]}


    template = loader.get_template('template1.html')

    documento = template.render(diccionario)

    return HttpResponse(documento)