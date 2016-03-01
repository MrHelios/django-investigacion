from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from usuarios.forms import Registrar_form

class UserPersonalView(View):

    template_name = "useraccount/registrar.html"

    def __init__(self):
        pass

    def get(self, request):
        if self.request.user.is_authenticated():
            return redirect("/usuario/lista")
        else:
            form = Registrar_form()
        return render(self.request, self.template_name, {'form' : form})

    def post(self, request):
        form = Registrar_form(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    form.cleaned_data['usuario'],
                    form.cleaned_data['email'],
                    form.cleaned_data['clave2'],
            )
            return redirect("/usuario/login")
        return render(self.request, self.template_name, {'form' : form})

class PruebaView(View):

    template_name = "useraccount/prueba.html"

    def get(self, request):
        usuario = User.objects.all()
        return render(self.request, self.template_name, {'usuario': usuario })

    def post(self, request):
        usuario = User.objects.all()
        respuesta = []
        for u in usuario:
            if request.POST.get(str(u),'') == 'on':
                respuesta.append(u)

        return render(self.request, self.template_name, {'usuario': usuario , 'respuesta': respuesta })

from django.http import HttpResponseRedirect

from .forms import UploadFileForm
from .models import UploadFile

class SubidaFileView(View):

    template_name = "useraccount/subir.html"

    def get(self, request):
        form = UploadFileForm()
        elementos = UploadFile.objects.all()
        return render(self.request, self.template_name, {'form': form, 'elementos': elementos})

    def post(self, request):
        form = UploadFileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            nuevo_arch = UploadFile(archivo = request.FILES['archivo'])
            nuevo_arch.save()
            return HttpResponseRedirect('/usuario/')
        else:
            return render(self.request, self.template_name, {'form': form})
