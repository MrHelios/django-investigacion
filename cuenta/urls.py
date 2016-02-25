from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^usuario/', include('usuarios.urls')),
    # Esto es agregado para el framework de User.account
    url(r'^account/', include('account.urls')),
]
