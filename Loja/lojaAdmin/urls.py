from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# --- CUSTOMIZAÇÃO DOS TEXTOS DA ÁREA ADMINISTRATIVA (CAPÍTULO 4) ---
admin.site.site_header = 'Gerenciamento da Loja Virtual'      # Texto da barra superior azul
admin.site.site_title = 'Loja Admin'                          # Título da aba do navegador
admin.site.index_title = 'Área Administrativa do Painel'      # Subtítulo da página inicial do admin