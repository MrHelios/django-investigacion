from django import forms
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

def index(request):

    if request.user.is_authenticated():
        usuario = request.user
    else:
        usuario = 'Anonimo'    

    if request.method == 'POST':
        respuesta = request.POST.get('algo','')
        return render(request,'HTML/resp-index.html', {'respuesta':respuesta, 'usuario': usuario})
    else:
        return render(request,'HTML/index.html', {'usuario': usuario})

from django.contrib.auth.models import User

def crear_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario','')
        clave = request.POST.get('clave','')
        clave2 = request.POST.get('clave2','')

        if User.objects.get(username=usuario):
            error_nombre = 'El nombre ya existe'
            return render(request, 'HTML/creacion-usuario.html',
                            {'error_nombre' : error_nombre})

        if clave == clave2:
            user = User.objects.create_user(usuario,'',clave)
            return HttpResponseRedirect('/usuario/lista/')
        else:
            error_clave = 'Las contraseñas son distintas'
            return render(request, 'HTML/creacion-usuario.html',
                            {'error_clave' : error_clave})
    else:
        return render(request, 'HTML/creacion-usuario.html')

def lista_usuario(request):
    mostrar_usuarios = User.objects.all()
    return render(request, 'HTML/lista.html', {'usuario':mostrar_usuarios})

from django.template.context import RequestContext
from .forms import Registrar_form

def crear_usuario_FORM(request):
    if request.method == 'POST':
        form = Registrar_form(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['usuario'],
                form.cleaned_data['email'],
                form.cleaned_data['clave2'],
            )
            return HttpResponseRedirect('/usuario/lista/')
        else:
            variable = RequestContext(request, {'form' : form})
    else:
        form = Registrar_form()
        variable = RequestContext(request, {'form' : form})
    return render_to_response('HTML/crear-user-form.html', variable)

from django.contrib.auth import authenticate, login

def sistema_login(request):
    form = Registrar_form()
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/usuario/')
        else:
            errors = True
            variable = RequestContext(request, { 'form': form, 'errors': errors })
    else:
        variable = RequestContext(request, { 'form': form })
    return render_to_response('HTML/login.html', variable)

from django.contrib.auth import logout

def sistema_logout(request):
    logout(request)
    return HttpResponseRedirect('/usuario/')
