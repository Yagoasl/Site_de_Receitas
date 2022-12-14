from django.contrib import admin
from .models import LivroReceitas

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita','categoria','tempo_de_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(LivroReceitas, ListandoReceitas)

#loguin localhost:8000/admin
#user = admin
#pass = 123456