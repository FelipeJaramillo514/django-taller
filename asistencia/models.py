from django.core.exceptions import ValidationError
from django.db import models


class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    fecha_asistencia = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha_asistencia", "nombre_completo"]
        verbose_name = "asistencia"
        verbose_name_plural = "asistencias"

    def clean(self):
        super().clean()
        if self.hora_ingreso and self.hora_salida and self.hora_salida <= self.hora_ingreso:
            raise ValidationError(
                {"hora_salida": "La hora de salida debe ser posterior a la hora de ingreso."}
            )

    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"

# Create your models here.
