from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrar/$', views.UserPersonalView.as_view()),
    url(r'^prueba/$', views.PruebaView.as_view()),
    url(r'^subir/$', views.SubidaFileView.as_view()),
    url(r'^subir/(?P<UploadFile_id>[0-9])/$', views.EditFileView.as_view()),
]
