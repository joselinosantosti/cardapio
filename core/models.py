from django.db import models
from django.db.models.fields import SlugField
from django.template import defaultfilters
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.categoria

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)