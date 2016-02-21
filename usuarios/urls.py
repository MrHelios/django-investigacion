from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^crear/$', views.crear_usuario, name='crear_usuario'),
    url(r'^crear-user-form/$', views.crear_usuario_FORM, name='crear_usuario_Form'),

    url(r'^lista/$', views.lista_usuario, name='lista_usuario'),
]
