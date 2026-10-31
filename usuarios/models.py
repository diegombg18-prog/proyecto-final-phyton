from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True, verbose_name="Imagen de Perfil")
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Señal para crear o actualizar el perfil automáticamente al registrar un usuario
@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()