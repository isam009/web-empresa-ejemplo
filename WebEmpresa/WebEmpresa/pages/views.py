from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id, page_slug):
    """Funcion para obtener el id de la pagina estatica que el usuario escogio

    Args:
        request (obj): Peticion
        page_id (int): Es el id para cada vinculo
        page_slug (String): Para la obtencion del slug 

    Returns:
        obj: El objeto qeu contiene todos los id de la tabla Page
    """
    
    page = get_object_or_404(Page, id = page_id)

    return render(request, 'pages/sample.html', {'page': page})