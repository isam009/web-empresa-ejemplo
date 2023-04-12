from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"),
    # path para agregar el id de page
    # Agregando int: para convertir la cadena que atrape a entero
]