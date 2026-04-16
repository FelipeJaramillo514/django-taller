from django.shortcuts import redirect, render

from .forms import SolicitudForm


def crear_solicitud(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("solicitudes:confirmacion")
    else:
        form = SolicitudForm()

    return render(request, "solicitudes/formulario.html", {"form": form})


def confirmacion_solicitud(request):
    return render(request, "solicitudes/confirmacion.html")

# Create your views here.
