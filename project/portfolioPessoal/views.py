from django.shortcuts import render
from .models import (
    Competencia, Docente, Tecnologia, Licenciatura, 
    UnidadeCurricular, TFC, Projeto, Formacao, Interesse, MakingOf
)

def portfolio_view(request):
    return render(request, 'portfoliopessoal/portfolio.html')

def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfoliopessoal/projetos.html', context)

def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfoliopessoal/tecnologias.html', context)

def licenciaturas_view(request):
    context = {'licenciaturas': Licenciatura.objects.all()}
    return render(request, 'portfoliopessoal/licenciaturas.html', context)

def ucs_view(request):
    context = {'ucs': UnidadeCurricular.objects.all()}
    return render(request, 'portfoliopessoal/ucs.html', context)

def tfcs_view(request):
    context = {'tfcs': TFC.objects.all()}
    return render(request, 'portfoliopessoal/tfc.html', context)

def docentes_view(request):
    context = {'docentes': Docente.objects.all()}
    return render(request, 'portfoliopessoal/docentes.html', context)

def competencias_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfoliopessoal/competencias.html', context)

def formacoes_view(request):
    context = {'formacoes': Formacao.objects.all()}
    return render(request, 'portfoliopessoal/formacoes.html', context)

def interesses_view(request):
    context = {'interesses': Interesse.objects.all()}
    return render(request, 'portfoliopessoal/interesses.html', context)

def makingof_view(request):
    # Usamos select_related para ir buscar o nome do projeto sem sobrecarregar a base de dados
    dados = MakingOf.objects.select_related('projeto').all()
    return render(request, 'portfoliopessoal/makingof.html', {'logs': dados})