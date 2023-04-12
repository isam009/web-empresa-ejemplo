from django.db import models

# Create your models here.
class Service(models.Model):
    """Model definition for Services."""

    title = models.CharField('Titulo', max_length=200)
    subtitle = models.CharField('Subtitulo', max_length=200)
    content = models.TextField('Contenido')
    image = models.ImageField('Imagen', upload_to="services", height_field=None, width_field=None, max_length=None)
    created = models.DateTimeField('Creado', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Actualizado', auto_now=True, auto_now_add=False)


    class Meta:
        """Meta definition for Services."""

        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['created']

    def __str__(self):
        """Unicode representation of Services."""
        return str(self.id) + '-' + self.title

