from django.contrib import admin
from django.urls import path
from loja.views import (
    home_view,
    list_produto_view, 
    edit_produto_view, 
    edit_produto_postback, 
    details_produto_view,
    delete_produto_view,
    delete_produto_postback
)

urlpatterns = [
    # Rota do Painel de Administração do Django
    path('admin/', admin.site.urls),

    # Rota da Home (Página Inicial)
    path("", home_view, name='home'),
    
    # Rotas do CRUD de Produtos
    path("produto", list_produto_view, name='produto'),
    path("produto/<int:id>", list_produto_view, name='produto_id'),
    path("produto/edit/<int:id>", edit_produto_view, name='edit_produto'),
    path("produto/edit", edit_produto_postback, name='edit_produto_postback'),
    path("produto/details/<int:id>", details_produto_view, name='details_produto'),
    path("produto/delete/<int:id>", delete_produto_view, name='delete_produto'),
    path("produto/delete", delete_produto_postback, name='delete_produto_postback'),
]