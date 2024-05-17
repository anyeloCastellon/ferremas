from django.db import models
from django.conf import settings
from base.models import BaseModel

class Contacto(BaseModel):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Usuario'
    )
    nombre_completo = models.CharField(max_length=255, verbose_name='Nombre Completo')
    motivo = models.CharField(max_length=100, verbose_name='Motivo', choices=[
        ('felicitacion', 'Felicitación'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
    ])
    mensaje = models.TextField(verbose_name='Mensaje')

    def __str__(self):
        # Incluye la representación del usuario si está disponible
        usuario_str = self.usuario.username if self.usuario else "Usuario Anónimo"
        return f"{usuario_str} - {self.nombre_completo} - {self.motivo}"

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['id']
