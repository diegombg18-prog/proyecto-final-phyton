from django.urls import path
from .views import (
    ListadoPostsView,
    DetallePostView,
    CrearPostView,
    EditarPostView,
    EliminarPostView,
    buscar_posts,
)

urlpatterns = [
    path('', ListadoPostsView.as_view(), name='listado_posts'),
    path('post/<int:pk>/', DetallePostView.as_view(), name='detalle_post'),
    path('post/nuevo/', CrearPostView.as_view(), name='crear_post'),
    path('post/<int:pk>/editar/', EditarPostView.as_view(), name='editar_post'),
    path('post/<int:pk>/borrar/', EliminarPostView.as_view(), name='eliminar_post'),
    path('buscar/', buscar_posts, name='buscar_posts'),
]