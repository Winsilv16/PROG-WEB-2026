from django.contrib import admin
from .models import Fabricante, Categoria, Produto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')       
    list_display_links = ('id', 'nome') 
    search_fields = ('nome',)           

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

# --- CUSTOMIZAÇÃO DO PRODUTO ---
class ProdutoAdmin(admin.ModelAdmin):
 
    list_display = ('id', 'produto', 'preco', 'estoque', 'fabricante', 'destaque', 'disponivel')
    list_display_links = ('id', 'produto')
    
    list_filter = ('fabricante', 'categoria', 'destaque', 'disponivel')
    
    list_editable = ('estoque', 'disponivel', 'destaque')
    
    search_fields = ('produto', 'descricao')

    list_per_page = 10

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Produto, ProdutoAdmin)