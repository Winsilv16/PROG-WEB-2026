from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from loja.models import Produto 

def home_view(request):
    return HttpResponse("<h1>Olá Mundo! (Home)</h1>")

def list_produto_view(request, id=None):
    # 1. Captura dos parâmetros vindos da URL via método GET
    produto_param = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    dias = request.GET.get("dias")

    # 2. Inicializa a QuerySet trazendo todos os produtos
    produtos = Produto.objects.all()

    # 3. Aplicação dos filtros do Django ORM
    if produto_param is not None:
        # Se no seu models.py o campo for 'produto' minúsculo:
        try:
            produtos = produtos.filter(produto__contains=produto_param)
        except Exception:
            # Caso o seu campo no models.py se chame 'nome', ele usa esse aqui:
            produtos = produtos.filter(nome__contains=produto_param)

    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)

    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)

    if id is not None:
        produtos = produtos.filter(id=id)

    # 4. Filtro por quantidade de dias cadastrados
    if dias is not None:
        try:
            now = timezone.now()
            now = now - timedelta(days=int(dias))
            produtos = produtos.filter(criado_em__gte=now)
        except Exception:
            pass

    # 5. Imprime o resultado do ORM no console do terminal
    print("\n========== [ CAPÍTULO 6 - ORM CONSOLE ] ==========")
    print(f"Produtos encontrados: {produtos}")
    print("==================================================\n")

    # Retorno visual padrão para o navegador
    id_exibicao = id if id is not None else 0
    return HttpResponse('<h1>Produto de id %s!</h1>' % id_exibicao)