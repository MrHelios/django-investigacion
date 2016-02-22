from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Sistema de creacion de cuenta
    url(r'^crear/$', views.crear_usuario, name='crear_usuario'),
    url(r'^crear-user-form/$', views.crear_usuario_FORM, name='crear_usuario_Form'),
    # Sistema de login
    url(r'^login/$', views.sistema_login, name='sistema_login'),
    url(r'^logout/$', views.sistema_logout, name='sistema_logout'),
    # Otros
    url(r'^lista/$', views.lista_usuario, name='lista_usuario'),
]
