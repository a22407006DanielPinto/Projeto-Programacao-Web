from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Competencia, Docente, Tecnologia, Licenciatura, 
    UnidadeCurricular, TFC, Projeto, Formacao, Interesse, MakingOf
)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

# PÁGINAS INICIAIS
def portfolio_view(request):
    return render(request, 'portfoliopessoal/portfolio.html')

def sobre_view(request):
    return render(request, 'portfoliopessoal/sobre.html')

# LISTAGENS
def projetos_view(request):
    return render(request, 'portfoliopessoal/projetos.html', {'projetos': Projeto.objects.all()})

def tecnologias_view(request):
    return render(request, 'portfoliopessoal/tecnologias.html', {'tecnologias': Tecnologia.objects.all()})

def licenciaturas_view(request):
    return render(request, 'portfoliopessoal/licenciaturas.html', {'licenciaturas': Licenciatura.objects.all()})

def ucs_view(request):
    return render(request, 'portfoliopessoal/ucs.html', {'ucs': UnidadeCurricular.objects.all()})

def tfcs_view(request):
    return render(request, 'portfoliopessoal/tfc.html', {'tfcs': TFC.objects.all()})

def docentes_view(request):
    return render(request, 'portfoliopessoal/docentes.html', {'docentes': Docente.objects.all()})

def competencias_view(request):
    return render(request, 'portfoliopessoal/competencias.html', {'competencias': Competencia.objects.all()})

def formacoes_view(request):
    return render(request, 'portfoliopessoal/formacoes.html', {'formacoes': Formacao.objects.all()})

def interesses_view(request):
    return render(request, 'portfoliopessoal/interesses.html', {'interesses': Interesse.objects.all()})

def makingof_view(request):
    dados = MakingOf.objects.select_related('projeto').all()
    return render(request, 'portfoliopessoal/makingof.html', {'logs': dados})

# CRUD: PROJETOS
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfoliopessoal/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})

def editar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfoliopessoal/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})

def apagar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfoliopessoal/projeto_confirmar_delete.html', {'projeto': projeto})

# CRUD: TECNOLOGIAS
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def editar_tecnologia_view(request, nome):
    tecnologia = get_object_or_404(Tecnologia, nomeTecnologia=nome)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def apagar_tecnologia_view(request, nome):
    tecnologia = get_object_or_404(Tecnologia, nomeTecnologia=nome)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_confirmar_delete.html', {'tecnologia': tecnologia})

# CRUD: COMPETÊNCIAS
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfoliopessoal/competencias_form.html', {'form': form, 'titulo': 'Nova Competência'})

def editar_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfoliopessoal/competencias_form.html', {'form': form, 'titulo': 'Editar Competência'})

def apagar_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfoliopessoal/competencias_confirmar_delete.html', {'competencia': competencia})

# CRUD: FORMAÇÃO
def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfoliopessoal/formacoes_form.html', {'form': form, 'titulo': 'Nova Formação'})

def editar_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfoliopessoal/formacoes_form.html', {'form': form, 'titulo': 'Editar Formação'})

def apagar_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfoliopessoal/formacoes_confirmar_delete.html', {'formacao': formacao})