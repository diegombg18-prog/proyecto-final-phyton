from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, perfil, editar_perfil

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
]