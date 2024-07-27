from django.shortcuts import render, get_object_or_404
from core.models import Product, Blog

def Home (request):
    data = {
        'title': 'GameVibes - Home',
        'Noticias': [
            {
                
            },
            {
                
            },
            {
                
            }
        ],
        'Reviews': [
             Reviews.objects.all()
        ]
    }
    
    return render(request, 'Reviews.html', data)

def review (request):
    data = {
        'title': 'GameVibes - Home',
        'Reviews': [
           Reviews.objects.all()
        ]
    }
    
    return render(request, 'Reviews.html', data)

def News (request):
    Noticias = News.objects.all()

    data = {
        'title': 'Noticias | GameVibes',
    }
    return render(request, 'produtos.html', data)

def Desconto (request):
        data = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
        'title': 'Descontos | GameVibes ',
    }
        return render(request, 'Descontos.html', data)	

def Desconto_single(request, id):
    product = get_object_or_404(Product, id=id) 
    return render(request, 'Descontos_single.html', {'desconto': product})  

def News_single(request):
    blog = Blog.objects.all()

    data = {
        'blog': blog,
        'title': 'TurboBrasil - Venha nos conhecer! | TurboBrasil'
    }
    return render(request, 'News_single.html', data)



def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})

