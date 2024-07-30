from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('descontos/', views.descontos_list, name='Descontos'),
    path('descontos/<slug:slug>/', views.descontos_detail, name='Descontos_single'),
    path('news/', views.news_list, name='News'),
    path('news/<slug:slug>/', views.news_detail, name='News_single'),
    path('reviews/', views.reviews_list, name='Reviews'),
    path('reviews/<slug:slug>/', views.reviews_detail, name='Reviews_single'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
