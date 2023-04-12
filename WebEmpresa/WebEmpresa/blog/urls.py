from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
    # path para agregar el id de categoria
    # Agregando int: para convertir la cadena que atrape a entero
]