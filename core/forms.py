from django import forms
from django.db.models import fields

from core.models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'preco', 'imagem']