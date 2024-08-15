from django.shortcuts import render, get_object_or_404
from .models import TipoCorreia, Formula

def home(request):
    tipos_correia = TipoCorreia.objects.all()
    formulas = Formula.objects.all()
    return render(request, 'home.html', {'tipos_correia': tipos_correia, 'formulas': formulas})

def lista_tipos_correia(request):
    tipos_correia = TipoCorreia.objects.all()
    return render(request, 'lista_tipos_correia.html', {'tipos_correia': tipos_correia})

def detalhe_tipo_correia(request, tipo_correia_id):
    tipo_correia = get_object_or_404(TipoCorreia, id=tipo_correia_id)
    return render(request, 'detalhe_tipo_correia.html', {'tipo_correia': tipo_correia})

def lista_formulas(request):
    formulas = Formula.objects.all()
    return render(request, 'lista_formulas.html', {'formulas': formulas})

def detalhe_formula(request, formula_id):
    formula = get_object_or_404(Formula, id=formula_id)
    return render(request, 'detalhe_formula.html', {'formula': formula})

def conclusao(request):
    return render(request, 'conclusao.html')
