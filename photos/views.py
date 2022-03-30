from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo


# Create your views here.
def saludo(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    return HttpResponse("Hello {0} {1}".format(nombre, apellido))


def home(request):
    """
    Renderiza el home con un lisado de fotos
    :param request: objeto HtttpRequest con los datos de la peticion
    :return: objeto HttpResponse con los datos de la respuesta
    """
    photos = Photo.objects.all() #Recupera todas las foos de la base de datos
    context = {'photos_list': photos}
    return render(request, 'photos/home.html', context)