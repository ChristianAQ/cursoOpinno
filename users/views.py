from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from users.forms import LoginForm
from django.views import View


class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario del login
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecta"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'photos_home'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('photos_home')




