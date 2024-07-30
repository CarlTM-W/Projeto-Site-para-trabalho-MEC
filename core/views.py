from django.shortcuts import render, get_object_or_404
from .models import Noticia, Review, Desconto

def home(request):
    noticias = Noticia.objects.all()
    reviews = Review.objects.all()
    return render(request, 'Home.html', {'Noticias': noticias, 'Reviews': reviews})

def descontos_list(request):
    descontos = Desconto.objects.all()
    return render(request, 'Descontos.html', {'Descontos': descontos})

def descontos_detail(request, slug):
    desconto = get_object_or_404(Desconto, slug=slug)
    return render(request, 'Descontos_single.html', {'desconto': desconto})

def news_list(request):
    noticias = Noticia.objects.all()
    return render(request, 'News.html', {'Noticias': noticias})

def news_detail(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'News_single.html', {'noticia': noticia})

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'Reviews.html', {'Reviews': reviews})

def reviews_detail(request, slug):
    review = get_object_or_404(Review, slug=slug)
    return render(request, 'Reviews_single.html', {'review': review})
