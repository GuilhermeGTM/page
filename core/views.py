from django.views.generic import ListView

from .models import Produto


class IndexListview(ListView):
    template_name = 'index.html'
    paginate_by = 5
    # para ordenar decrescente coloca -
    # tipos para ordenar id, nome, preco
    ordering = 'id'
    model = Produto
