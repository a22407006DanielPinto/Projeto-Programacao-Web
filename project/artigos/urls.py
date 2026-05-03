from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos_view, name='lista_artigos'),
    path('<int:id>/', views.detalhe_artigo_view, name='detalhe_artigo'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('<int:id>/editar/', views.editar_artigo_view, name='editar_artigo'),
    path('<int:id>/apagar/', views.apagar_artigo_view, name='apagar_artigo'),
    path('<int:id>/like/', views.like_artigo_view, name='like_artigo'),
]