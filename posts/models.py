from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Subtítulo")
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Imagen del Post")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Autor")

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo