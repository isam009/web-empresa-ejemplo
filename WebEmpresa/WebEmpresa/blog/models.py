from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Para importar todos los usuarios del admin y utilizarlos en el objeto User

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField('Nombre', max_length=100)
    created = models.DateTimeField('Creado', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Actualizado', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Category."""
        return str(self.id) + '-' + self.name

class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField('Titulo', max_length=50)
    content = models.TextField('Contenido')
    published = models.DateTimeField('Publicado', default=timezone.now) #timezone.now es un metodo para agregar la hora actual
    image = models.ImageField('Imagen', upload_to='blog', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE) #User lo usamos como paramaetros para que cada usuario lo agregue como autor de cada entrada
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") # related_name es el nombre de la relacion 
    created = models.DateTimeField('Creado', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Actualizado', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Post."""
        return str(self.id) + '-' + self.title
