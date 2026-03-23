from django.contrib import admin
from .models import Libro
from .models import Autore
from .models import Lingua_og

# admin.site.register(Libro)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'autore', 'anno']
    list_filter = ['autore', 'anno']
    search_fields = ['titolo', 'autore']


admin.site.register(Autore)
admin.site.register(Lingua_og)



# Register your models here.
