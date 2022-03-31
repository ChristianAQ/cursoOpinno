from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, VISIBILITY_PUBLIC


# Create your views here.
def saludo(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    return HttpResponse("Hello {0} {1}".format(nombre, apellido))


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HtttpRequest con los datos de la peticion
    :return: objeto HttpResponse con los datos de la respuesta
    """
    # Recupera todas las fotos de la base de datos
    photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
    context = {'photos_list': photos[:2]}
    return render(request, 'photos/home.html', context)

def photo_detail(request, pk):
    """
        Renderiza el home con un listado de fotos
        :param request: objeto HtttpRequest con los datos de la peticion
        :param pk: clave primaria de la foto a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
    """
    #es como hacer un join en la peticion a la base de datos .select_related("owner")
    possible_photos = Photo.objects.filter(pk=pk).select_related("owner")
    if len(possible_photos) == 0:
        #por si no tiene foto ese id
        return HttpResponseNotFound("La imagen que buscas no existe")
    elif len(possible_photos) > 1:
        #por si tiene varias fotos
        return HttpResponse("Multiples opciones", status=300)

    photo = possible_photos[0]
    context = {'photo':photo}
    return render(request, 'photos/photo_detail.html', context)

