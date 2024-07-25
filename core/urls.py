from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import index, contato, produtos, produto_single, blogs, blog_single

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produtos', produtos, name='produtos'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blogs, name='blogs'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



