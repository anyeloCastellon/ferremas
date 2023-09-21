from django.db import models
from base.models import BaseModel


class RegistroHistorico(BaseModel):
    timestamp = models.DateTimeField()
    estado = models.BooleanField()  # True para arriba, False para abajo
    escalado_a = models.CharField(max_length=50, choices=[('cliente', 'Cliente'), ('interno', 'Interno'), ('infraestructura', 'Infraestructura'), ('Sin Gestión', 'Sin Gestión')], null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    name_log_source = models.ForeignKey(
        "log_source.LogSource",
        on_delete=models.CASCADE,
        )

    company = models.ForeignKey(
        "user_management.Company",
        on_delete=models.CASCADE
        )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.name_log_source.name_log_source} - {self.timestamp} - {'Arriba' if self.estado else 'Abajo'}"
