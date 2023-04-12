from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id): # Creando funcion para tomar la id de la categoria
    
    category = get_object_or_404(Category, id = category_id) # Obteniendo el valor de la id que se obtiene de la url segun lo que escoja el usuario y guardandolo en la variable category
    return render(request, "blog/category.html", {'category': category})
