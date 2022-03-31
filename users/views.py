from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def login(request):
    """
    Presena el formulario del logun y gestuina el login de un usuario
    :param request: objeto HtttpRequest con los datos de la peticion
    :return: objeto HttpResponse con los datos de la respuesta
    """
    error_message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message = "Usuario o contraseña incorrecta"
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                error_message = "Cuenta de usuario inactiva"

    return render(request, 'users/login.html', {'error': error_message})


def logout(request):
    """
    Hace el logout de un usuario y redirige al login
    :param request: objeto HtttpRequest con los datos de la peticion
    :return: objeto HttpResponse con los datos de la respuesta
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('/')
