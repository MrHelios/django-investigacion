from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class Registrar_form(forms.Form):
    usuario = forms.CharField(max_length=30)
    email = forms.EmailField(label='Email')
    clave = forms.CharField(label='Password', widget=forms.PasswordInput())
    clave2 = forms.CharField(label='Password (Otra vez)', widget=forms.PasswordInput())

    def clean_usuario(self):
        '''
        Verifica que no exista un usuario con ese nombre.
        '''
        usuario = self.cleaned_data.get('usuario')
        try:
            if User.objects.get(username=usuario):
                raise forms.ValidationError('El nombre de usuario ya existe.')
        except ObjectDoesNotExist:
            return usuario

    def clean_clave2(self):
        clave = self.cleaned_data['clave']
        clave2 = self.cleaned_data['clave2']
        '''
        Verifica que las contraseñas sean iguales.
        '''
        if clave != clave2:
            raise forms.ValidationError('Las contraseñas son distintas.')
        '''
        Verifica la longitud de la contraseña.
        '''
        if len(clave2)<=2:
            raise forms.ValidationError('La contraseña es muy cortita.')
        return clave2
