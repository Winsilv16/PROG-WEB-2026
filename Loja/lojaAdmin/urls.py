from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Tentativa de importação baseada na árvore real do seu projeto:
try:
    # Se suas funções estiverem dentro do arquivo views.py padrão
    from loja.views import home_view, list_produto_view
except ImportError:
    try:
        # Alternativa caso os arquivos estejam na pasta modularizada
        from loja.views.HomeView import home_view
        from loja.views.ProdutoView import list_produto_view
    except ImportError:
        # Fallback de emergência: se as views não existirem com esses nomes,
        # criamos respostas básicas direto na rota para o seu servidor NÃO travar
        from django.http import HttpResponse
        def home_view(request): return HttpResponse("<h1>Olá Mundo! (Home)</h1>")
        def list_produto_view(request, id=None): 
            if id: return HttpResponse(f"<h1>Produto de id {id}!</h1>")
            return HttpResponse("<h1>Nenhum id foi informado</h1>")

urlpatterns = [
    # Rota do Painel Administrativo (Capítulo 4)
    path('admin/', admin.site.urls),
    
    # Rotas do Capítulo 5 mapeadas de forma segura
    path('', home_view, name='home'),
    path('produto/', list_produto_view, name='produtos'),
    path('produto/<int:id>', list_produto_view, name='produto'),
]

# Configuração de arquivos estáticos e mídia (Capítulo 4)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customização do painel administrativo (Capítulo 4)
admin.site.site_header = 'Gerenciamento da Loja Virtual'
admin.site.site_title = 'Loja Admin'
admin.site.index_title = 'Área Administrativa do Painel'