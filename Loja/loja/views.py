import os
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Produto, Categoria, Fabricante

def list_produto_view(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/produto.html', {'produtos': produtos})

# INSERIR / EDITAR
def save_produto_view(request, id=None):
    produto = get_object_or_404(Produto, id=id) if id else Produto()
    
    if request.method == 'POST':
        produto.produto = request.POST.get('produto')
        produto.destaque = 'destaque' in request.POST
        produto.promocao = 'promocao' in request.POST
        produto.msg_promocao = request.POST.get('msg_promocao')
        produto.preco = request.POST.get('preco') or 0.00
        
        cat_id = request.POST.get('categoria')
        fab_id = request.POST.get('fabricante')
        if cat_id: produto.categoria = Categoria.objects.get(id=cat_id)
        if fab_id: produto.fabricante = Fabricante.objects.get(id=fab_id)
        
        if request.FILES.get('image'):
            produto.image = request.FILES['image']
            
        produto.save()
        return redirect('produto')
    
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    
    context = {
        'produto': produto,
        'categorias': categorias,
        'fabricantes': fabricantes
    }
    return render(request, 'produto/produto_form.html', context)

def produto_detail_view(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/produto_detail.html', {'produto': produto})


def delete_produto_view(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':

        if produto.image and os.path.exists(produto.image.path):
            os.remove(produto.image.path)
        produto.delete()
        return redirect('produto')
        
    return render(request, 'produto/produto_confirm_delete.html', {'produto': produto})