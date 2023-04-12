from django.http import HttpRequest
from django.template import Template, context
from django.template import loader

def ProbandoTemplate(request):

    diccionario = {"nombre":"David","apellido":"Cerda","edad":32}

    archivo = open(r"C:\Users\David\Desktop\Tercera-pre-entrega-David-Cerda\ProyectoDjango\plantilla\template1.html")

    texto = archivo.read()
    archivo.close()

    templatE = Template(texto)
    contexto = context(diccionario)

    documento = Template.render(texto)
    
    return HttpRequest(documento)