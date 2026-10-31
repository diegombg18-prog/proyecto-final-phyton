from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de la app de publicaciones
    path('', include('posts.urls')),
    # Rutas de la app de usuarios (Login, Registro, Perfil)
    path('usuarios/', include('usuarios.urls')),
]

# Configuración esencial para que las imágenes se vean correctamente en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)