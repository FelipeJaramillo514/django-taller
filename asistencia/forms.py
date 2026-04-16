import re

from django import forms

from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            "nombre_completo",
            "documento_identidad",
            "correo_electronico",
            "fecha_asistencia",
            "hora_ingreso",
            "hora_salida",
            "presente",
            "observaciones",
        ]
        labels = {
            "nombre_completo": "Nombre completo",
            "documento_identidad": "Documento de identidad",
            "correo_electronico": "Correo electrónico",
            "fecha_asistencia": "Fecha de asistencia",
            "hora_ingreso": "Hora de ingreso",
            "hora_salida": "Hora de salida",
            "presente": "Presente",
            "observaciones": "Observaciones",
        }
        widgets = {
            "fecha_asistencia": forms.DateInput(attrs={"type": "date"}),
            "hora_ingreso": forms.TimeInput(attrs={"type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "observaciones": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_documento_identidad(self):
        documento = self.cleaned_data["documento_identidad"].strip()
        if not re.fullmatch(r"[0-9A-Za-z]+", documento):
            raise forms.ValidationError("El documento solo puede contener letras y números.")
        return documento
