from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from loja.views import (
    list_produto_view,
    save_produto_view,
    produto_detail_view,
    delete_produto_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_produto_view, name='home'), # Página inicial vai direto para a lista
    path('produto', list_produto_view, name='produto'),
    path('produto/novo', save_produto_view, name='create_produto'),
    path('produto/<int:id>', produto_detail_view, name='produto_detail'),
    path('produto/editar/<int:id>', save_produto_view, name='edit_produto'),
    path('produto/excluir/<int:id>', delete_produto_view, name='delete_produto'),
]

# Permite que o Django sirva os arquivos de mídia (Imagens) durante o desenvolvimento [cite: 4]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)