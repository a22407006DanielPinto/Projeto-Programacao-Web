from django.urls import path
from . import views

urlpatterns = [
    # PÁGINA PRINCIPAL E SOBRE
    path('', views.portfolio_view, name='portfolio'),
    path('sobre/', views.sobre_view, name='sobre'),

    # PROJETOS (CRUD)
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/editar/<int:id>/', views.editar_projeto_view, name='editar_projeto'),
    path('projeto/apagar/<int:id>/', views.apagar_projeto_view, name='apagar_projeto'),

    # TECNOLOGIAS (CRUD)
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/editar/<str:nome>/', views.editar_tecnologia_view, name='editar_tecnologia'),
    path('tecnologia/apagar/<str:nome>/', views.apagar_tecnologia_view, name='apagar_tecnologia'),

    # COMPETENCIAS (CRUD)
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/editar/<int:id>/', views.editar_competencia_view, name='editar_competencia'),
    path('competencia/apagar/<int:id>/', views.apagar_competencia_view, name='apagar_competencia'),

    # FORMAÇÃO (CRUD)
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/nova/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/editar/<int:id>/', views.editar_formacao_view, name='editar_formacao'),
    path('formacao/apagar/<int:id>/', views.apagar_formacao_view, name='apagar_formacao'),

    # LISTAGENS
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfc/', views.tfcs_view, name='tfc'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('makingof/', views.makingof_view, name='makingof'),
]