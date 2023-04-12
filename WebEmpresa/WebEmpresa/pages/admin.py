from django.contrib import admin
from .models import Page

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    '''Admin View for Page'''

    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')