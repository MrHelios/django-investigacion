from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        respuesta = request.POST.get('algo','')
        return render(request,'HTML/resp-index.html',{'respuesta':respuesta})
    else:
        return render(request,'HTML/index.html')

    return render(request,'HTML/index.html')

from django.contrib.auth.models import User

def crear_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario','')
        clave = request.POST.get('clave','')

        user = User.objects.create_user(usuario,'',clave)

        return HttpResponseRedirect('/usuario/lista/')
    else:
        return render(request, 'HTML/creacion-usuario.html')

def lista_usuario(request):
    mostrar_usuarios = User.objects.all()
    return render(request, 'HTML/lista.html', {'usuario':mostrar_usuarios})
