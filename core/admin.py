from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'slug', 'criado', 'modificado', 'ativo')

admin.site.register(Categoria)