from django.db import models
from .Categoria import Categoria
from .Fabricante import Fabricante

class Produto(models.Model):
    produto = models.CharField(max_length=200)
    preco = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, verbose_name='Preço')
    descricao = models.TextField(default='')
    estoque = models.IntegerField(default=0)
    destaque = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'