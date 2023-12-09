# models.py

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('C', 'Completado'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, help_text="Ingrese el título de la tarea.")
    descripcion = models.TextField(help_text="Ingrese la descripción de la tarea.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def clean(self):
        # Validación personalizada
        if self.estado == 'C' and not self.descripcion:
            raise ValidationError({'descripcion': 'La descripción es obligatoria para tareas completadas.'})
