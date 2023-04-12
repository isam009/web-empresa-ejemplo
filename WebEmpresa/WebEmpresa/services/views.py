from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):

    service = Service.objects.all()
    # Accediendo al atributo objets y ejecutando el metodo all() que nos va a traer todos los objetos de la db
    return render(request, "services/services.html", {"service": service})