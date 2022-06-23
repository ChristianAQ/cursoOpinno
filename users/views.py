from datetime import timezone

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.forms import LoginForm
from django.views import View

from users.models import Usuario


@api_view(['POST'])
def Login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")

    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
        return Response("Contraseña Inválida")

    token, _ = Token.objects.get_or_create(user=user)
    #print(token.key)
    return Response(token.key)

class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario del login
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'login_form': login_form}
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
        context = {'error': error_message, 'login_form': login_form}
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


def Signup(request):
    idUsuario = 0
    tipo=""
    email=""
    existe=0
    if request.method=='POST':
        print("HA ENTRADO EN EL POST")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("FORMULARIO VÁLIDO")
            tipo = request.POST.get('tipo')
            print("TIPO=="+str(tipo))

            buscaemail = request.POST.get('mail')
            print("EMAIL==="+str(buscaemail))

            resultado=User.objects.filter(email=buscaemail).exists();
            if resultado==True:
                print("existe el email")
                mensaje="El email" + str(buscaemail)+"ya existe registrado en el sistema"
                return render(request, 'registrarseylogin/existe_usuario.html', {'mensaje':mensaje})
            else:
                print("No existe el email. continuamos")

                request.session['usuario']=request.POST.get('username')
                print("USUARIO PARA REGISTRAR = "+str(request.session['usuario']))

                request.user.is_active = True
                request.user.is_staff = False
                request.user.is_superuser = False
                form.save(commit=True)

                usuario=User.objects.all().last()
                print('idUSUARIO ultimo actual='+str(usuario.id))
                idUsuario=int(usuario.id)

                print("cliente >>>"+str(idUsuario))
                try:
                    usuarionuevo = Usuario()
                    usuarionuevo.user_id = int(idUsuario)
                    usuarionuevo.conectado = True
                    usuarionuevo.ip = "0"
                    usuarionuevo.email = email
                    usuarionuevo.fecha_alta = timezone.now()
                    usuarionuevo.save()
                    print("registro del cliente guardado OK....")
                except:
                    print("Error al guardar al nuevo cliente")

                nombreusuario=request.session['usuario']
                print("email enviado OK....")
                return redirect('/')
    else:
        form = UserCreationForm()
        print("ENTRA EN ELSE PORQUE ES METODO GET")
    return render(request, 'users/signup.html', {'form': form})







