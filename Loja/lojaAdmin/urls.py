from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importa as views diretamente do arquivo loja/views.py
from loja.views import home_view, list_produto_view

urlpatterns = [
    # Rota do Painel Administrativo
    path('admin/', admin.site.urls),
    
    # IMPORTANTE: Colocamos os caminhos de produtos primeiro para o Django não se confundir
    path('produto/', list_produto_view, name='produtos'),
    path('produto/<int:id>', list_produto_view, name='produto'),
    
    # A página inicial (vazia) fica por último
    path('', home_view, name='home'),
]

# Configuração de arquivos estáticos e mídia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customização visual do painel admin
admin.site.site_header = 'Gerenciamento da Loja Virtual'
admin.site.site_title = 'Loja Admin'
admin.site.index_title = 'Área Administrativa do Painel'