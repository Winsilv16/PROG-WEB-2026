from django.shortcuts import render, redirect
from loja.models import Produto
from datetime import timedelta
from django.utils import timezone

# ==========================================
# 1. VIEW DA PÁGINA INICIAL (HOME)
# ==========================================
def home_view(request):
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    
    context = {
        'produtos': produtos
    }
    return render(request, template_name='home/home.html', context=context, status=200)


# ==========================================
# 2. VIEWS DO CRUD DE PRODUTOS
# ==========================================

# Listar Produtos (GET)
def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    
    produtos = Produto.objects.all()
    
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if dias is not None:
        now = timezone.now() - timedelta(days=int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if id is not None:
        produtos = produtos.filter(id=id)
        
    context = { 'produtos': produtos }
    return render(request, template_name='produto/produto.html', context=context, status=200)

# Interface Editar (GET)
def edit_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first()
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)

# Salvar Edição (POST)
def edit_produto_postback(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
            obj_produto.save()
        except Exception as e:
            print("Erro salvando edição: %s" % e)
            
    return redirect("/produto")

# Ver Detalhes (GET)
def details_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first()
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-details.html', context=context, status=200)

# Interface Apagar (GET)
def delete_produto_view(request, id=None):
    produto = Produto.objects.filter(id=id).first()
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-delete.html', context=context, status=200)

# Efetivar Exclusão (POST)
def delete_produto_postback(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            if obj_produto:
                obj_produto.delete()
        except Exception as e:
            print("Erro ao excluir produto: %s" % e)
            
    return redirect("/produto")