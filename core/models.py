from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    not_desc = models.TextField()
    not_image = models.ImageField(upload_to='noticias/')
    data = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Noticia, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Review(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    rev_desc = models.TextField()
    rev_image = models.ImageField(upload_to='reviews/')
    data = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
