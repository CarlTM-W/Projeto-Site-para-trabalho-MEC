from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tipos-correia/', views.lista_tipos_correia, name='lista_tipos_correia'),
    path('tipos-correia/<int:tipo_correia_id>/', views.detalhe_tipo_correia, name='detalhe_tipo_correia'),
    path('formulas/', views.lista_formulas, name='lista_formulas'),
    path('formulas/<int:formula_id>/', views.detalhe_formula, name='detalhe_formula'),
    path('conclusao/', views.conclusao, name='conclusao'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
