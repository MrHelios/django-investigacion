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
        return render()

    def post(self, request):
        return render()
