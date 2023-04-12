from django.contrib import admin
from .models import Category, Post

# Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    '''Admin View for category'''

    readonly_fields = ('created', 'updated')

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    '''Admin View for post'''

    list_display = ('title', 'author', 'published', 'post_categories')
    readonly_fields = ('created', 'updated')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username')
    # Si queremos buscar en campos de modelos relacionados entonces debemos indicar exactamente el nombre del campo dentro del modelo 
    #... como en este caso author es un campo relacionado entonces dentro de autor hay un campo username que contiene el nombre de autor.
    date_hierarchy = 'published' # Es un filtro por fecha muy util a al hora de trabajar con tablas grandes
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj): # Metodo para crear nuestro propio campo en el admin
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
        # Retorna una cadena de caracteres con los nombre de todas las categorias separadas por comas
    post_categories.short_description = "Categorias" # Para cambiarle el nombre por defecto del campo que hemos creado.