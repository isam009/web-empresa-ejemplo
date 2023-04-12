from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    """Model definition for Pages."""

    title = models.CharField('Titulo', max_length=200)
    content = RichTextField('Contenido')
    order = models.SmallIntegerField('Orden', default=0) #? Creamos el campo de entero pequenio order para ordenar la posicion de los enlaces a paginas estaticas
    created = models.DateTimeField('Created', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Actualizado', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Pages."""

        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']

    def __str__(self):
        """Unicode representation of Pages."""
        return str(self.id) + '-' + self.title

