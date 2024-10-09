from django.http import HttpResponse


def helloWorld(request):
    #Request es petición
    #Devolvemos una respuesta a la petición
    return HttpResponse("Hola mundo")

def ByeWorld(request):
    #Request es petición
    #Devolvemos una respuesta a la petición
    return HttpResponse("Adios mundo")