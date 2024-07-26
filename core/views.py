from django.shortcuts import render, get_object_or_404
from core.models import Product, Blog

def index (request):
    data = {
        'title': 'TurboBrasil - Home',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
        'news': [
            {
                'title': 'Nova versão do Django lançada!',
                'subtitle': 'Confira as novidades da versão 3.0',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero ut imperdiet vehicula.'
            },
            {
                'title': 'Python é a linguagem do futuro',
                'subtitle': 'Especialistas afirmam que Python está dominando o mercado',
                'text': 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
            },
            {
                'title': 'JavaScript: O que esperar do ES10?',
                'subtitle': 'Novas funcionalidades e melhorias na performance',
                'text': 'Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'
            }
        ]
    }
    
    return render(request, 'index.html', data)

def produtos (request):
    product = Product.objects.all()

    data = {
        'product': product,
        'title': 'TurboBrasil - Os melhores preços do Brasil | TurboBrasil',
    }
    return render(request, 'produtos.html', data)

def contato (request):
        data = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
        'title': 'Contato | TurboBrasil ',
    }
        return render(request, 'about.html', data)	

def produto_single(request, id):
    product = get_object_or_404(Product, id=id) # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'product': product})  

def blogs(request):
    blog = Blog.objects.all()

    data = {
        'blog': blog,
        'title': 'TurboBrasil - Venha nos conhecer! | TurboBrasil'
    }
    return render(request, 'blogs.html', data)



def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})

