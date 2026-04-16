import shutil
import tempfile
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Solicitud


TEST_MEDIA_ROOT = tempfile.mkdtemp(prefix="test_media_", dir=Path(__file__).resolve().parent.parent)


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class SolicitudViewsTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEST_MEDIA_ROOT, ignore_errors=True)

    def test_muestra_el_formulario_de_solicitudes(self):
        response = self.client.get(reverse("solicitudes:formulario"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Formulario de solicitud")
        self.assertContains(response, "Tipo de solicitud")

    def test_guarda_una_solicitud_valida_y_redirige_a_confirmacion(self):
        archivo = SimpleUploadedFile(
            "solicitud.pdf",
            b"%PDF-1.4 archivo de prueba",
            content_type="application/pdf",
        )

        response = self.client.post(
            reverse("solicitudes:formulario"),
            data={
                "nombre_solicitante": "Carlos Ruiz",
                "documento_identidad": "CC123456",
                "correo_electronico": "carlos@example.com",
                "telefono_contacto": "3001234567",
                "tipo_solicitud": "tecnica",
                "asunto": "Acceso a plataforma",
                "descripcion_detallada": "No puedo ingresar a mi cuenta institucional.",
                "fecha_solicitud": "2026-04-16",
                "archivo_adjunto": archivo,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("solicitudes:confirmacion"))
        self.assertContains(response, "La solicitud fue enviada y quedó almacenada correctamente.")
        self.assertEqual(Solicitud.objects.count(), 1)
        solicitud = Solicitud.objects.get()
        self.assertEqual(solicitud.tipo_solicitud, "tecnica")
        self.assertTrue(solicitud.archivo_adjunto.name.startswith("solicitudes/"))

    def test_rechaza_un_archivo_con_extension_no_permitida(self):
        archivo = SimpleUploadedFile(
            "script.exe",
            b"contenido invalido",
            content_type="application/octet-stream",
        )

        response = self.client.post(
            reverse("solicitudes:formulario"),
            data={
                "nombre_solicitante": "Maria Lopez",
                "documento_identidad": "ID9090",
                "correo_electronico": "maria@example.com",
                "telefono_contacto": "3105556677",
                "tipo_solicitud": "administrativa",
                "asunto": "Certificado",
                "descripcion_detallada": "Necesito un certificado actualizado.",
                "fecha_solicitud": "2026-04-16",
                "archivo_adjunto": archivo,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Adjunta un archivo PDF, DOC, DOCX, PNG o JPG.")
        self.assertEqual(Solicitud.objects.count(), 0)

# Create your tests here.
