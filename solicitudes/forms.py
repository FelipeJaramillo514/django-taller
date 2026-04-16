import re
from pathlib import Path

from django import forms

from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "nombre_solicitante",
            "documento_identidad",
            "correo_electronico",
            "telefono_contacto",
            "tipo_solicitud",
            "asunto",
            "descripcion_detallada",
            "fecha_solicitud",
            "archivo_adjunto",
        ]
        labels = {
            "nombre_solicitante": "Nombre del solicitante",
            "documento_identidad": "Documento de identidad",
            "correo_electronico": "Correo electrónico",
            "telefono_contacto": "Teléfono de contacto",
            "tipo_solicitud": "Tipo de solicitud",
            "asunto": "Asunto",
            "descripcion_detallada": "Descripción detallada",
            "fecha_solicitud": "Fecha de la solicitud",
            "archivo_adjunto": "Archivo adjunto",
        }
        widgets = {
            "telefono_contacto": forms.NumberInput(attrs={"min": 1000000}),
            "descripcion_detallada": forms.Textarea(attrs={"rows": 5}),
            "fecha_solicitud": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_documento_identidad(self):
        documento = self.cleaned_data["documento_identidad"].strip()
        if not re.fullmatch(r"[0-9A-Za-z]+", documento):
            raise forms.ValidationError("El documento solo puede contener letras y números.")
        return documento

    def clean_telefono_contacto(self):
        telefono = str(self.cleaned_data["telefono_contacto"])
        if not 7 <= len(telefono) <= 15:
            raise forms.ValidationError("Ingresa un número telefónico válido de 7 a 15 dígitos.")
        return self.cleaned_data["telefono_contacto"]

    def clean_archivo_adjunto(self):
        archivo = self.cleaned_data.get("archivo_adjunto")
        if not archivo:
            return archivo

        extensiones_permitidas = {".pdf", ".doc", ".docx", ".png", ".jpg", ".jpeg"}
        extension = Path(archivo.name).suffix.lower()

        if extension not in extensiones_permitidas:
            raise forms.ValidationError("Adjunta un archivo PDF, DOC, DOCX, PNG o JPG.")

        if archivo.size > 5 * 1024 * 1024:
            raise forms.ValidationError("El archivo adjunto no debe superar los 5 MB.")

        return archivo
