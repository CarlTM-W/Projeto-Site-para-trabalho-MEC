from django.db import models
from django.db import models
#slug
from django.utils.text import slugify
#format_html pra exibir a imagem em miniatura
from django.utils.html import format_html

class Category(models.Model):
    cat_name = models.CharField('Nome', unique=True, max_length=255)
    slug = models.SlugField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.cat_name)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
       return self.cat_name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Marca(models.Model):
    mac_name = models.CharField('Nome', unique=True, max_length=255, blank=False, null=False)
    mac_image = models.ImageField('Imagem da marca', upload_to='images/marcas', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.mac_name)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
       return self.mac_name

    def mini_image(self):
        if self.mac_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.cat_image.url)
        return " "
    mini_image.short_description = 'Imagem da marca'

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Product (models.Model):
    name = models.CharField('Nome', unique=True, max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    stock = models.IntegerField('Quantidade em Estoque', null=True, blank=True)
    descricao = models.TextField('Descricao do Produto', null=True, blank=True)
    ano = models.IntegerField('Ano do carro', null=False, blank=False)
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    pro_mac = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    image = models.ImageField('Imagem de capa', upload_to='images/produto', blank=True, null=True)
    slug = models.SlugField( null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100, blank=True, null=True)
    blo_description = models.TextField('Texto do Blog')
    blo_image = models.ImageField('Imagem de Capa', upload_to='images/blog', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blo_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def mini_image(self):
        if self.blo_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.blo_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'

    def __str__(self):
       return self.blo_title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
