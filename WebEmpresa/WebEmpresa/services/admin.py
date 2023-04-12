from django.contrib import admin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    readonly_fields = ('created', 'updated',)