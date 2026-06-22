from django.contrib import admin
from .models import Fabricante, Categoria, Produto

# --- CUSTOMIZAÇÃO DA CATEGORIA ---
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')       # Exibe o ID e o Nome em colunas
    list_display_links = ('id', 'nome') # Clicar no ID ou no Nome abre a edição
    search_fields = ('nome',)           # Cria uma barra de pesquisa por nome

# --- CUSTOMIZAÇÃO DO FABRICANTE ---
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

# --- CUSTOMIZAÇÃO DO PRODUTO ---
class ProdutoAdmin(admin.ModelAdmin):
    # Mostra colunas com detalhes importantes do produto na listagem principal
    list_display = ('id', 'produto', 'preco', 'estoque', 'fabricante', 'destaque', 'disponivel')
    list_display_links = ('id', 'produto')
    
    # Cria filtros inteligentes na lateral direita do painel
    list_filter = ('fabricante', 'categoria', 'destaque', 'disponivel')
    
    # Permite alterar o estoque, destaque e disponibilidade direto na tabela, sem abrir o produto
    list_editable = ('estoque', 'disponivel', 'destaque')
    
    # Adiciona campo de busca por nome do produto ou descrição
    search_fields = ('produto', 'descricao')
    
    # Define o limite de 10 produtos exibidos por página (paginação)
    list_per_page = 10

# --- REGISTRO DOS MODELOS COM AS NOVAS CONFIGURAÇÕES ---
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Produto, ProdutoAdmin)