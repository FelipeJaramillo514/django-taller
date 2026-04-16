from django.test import TestCase
from django.urls import reverse

from .models import Asistencia


class AsistenciaViewsTests(TestCase):
    def test_muestra_el_formulario_de_asistencia(self):
        response = self.client.get(reverse("asistencia:registro"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registro de asistencia")
        self.assertContains(response, "Nombre completo")

    def test_guarda_una_asistencia_valida_y_redirige_a_confirmacion(self):
        response = self.client.post(
            reverse("asistencia:registro"),
            data={
                "nombre_completo": "Ana Perez",
                "documento_identidad": "ABC12345",
                "correo_electronico": "ana@example.com",
                "fecha_asistencia": "2026-04-16",
                "hora_ingreso": "08:00",
                "hora_salida": "10:00",
                "presente": "on",
                "observaciones": "Llego puntual.",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("asistencia:confirmacion"))
        self.assertContains(response, "La asistencia fue almacenada correctamente")
        self.assertEqual(Asistencia.objects.count(), 1)
        registro = Asistencia.objects.get()
        self.assertEqual(registro.nombre_completo, "Ana Perez")
        self.assertTrue(registro.presente)

    def test_no_guarda_si_la_hora_de_salida_no_supera_la_hora_de_ingreso(self):
        response = self.client.post(
            reverse("asistencia:registro"),
            data={
                "nombre_completo": "Luis Gomez",
                "documento_identidad": "ZX9876",
                "correo_electronico": "luis@example.com",
                "fecha_asistencia": "2026-04-16",
                "hora_ingreso": "11:00",
                "hora_salida": "10:30",
                "presente": "on",
                "observaciones": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La hora de salida debe ser posterior a la hora de ingreso.")
        self.assertEqual(Asistencia.objects.count(), 0)

# Create your tests here.
