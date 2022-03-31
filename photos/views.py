from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, VISIBILITY_PUBLIC
from photos.forms import PhotoForm
from django.contrib.auth.decorators import login_required

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
    context = {'photos_list': photos[:4]}
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


@login_required()
def photo_creation(request):
    """
        Presenta al formulario para cerar una foto y en caso ed que la peticion sea POST la valida
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
    """
    message = None
    if request.method == "POST":
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance=photo_with_user)
        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()
            message = 'Foto creada satisfactoriamente <a href="/photos/{0}">Ver Foto</a>'.format(new_photo.pk)
    else:
        photo_form = PhotoForm()
    context = {'form': photo_form, 'message': message}
    return render(request, 'photos/photo_creation.html', context)
