from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import (
    Competencia, Docente, Tecnologia, Licenciatura,
    UnidadeCurricular, TFC, Projeto, Formacao, Interesse, MakingOf
)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

def is_gestor(user):
    return user.is_authenticated and user.groups.filter(name='gestor-portfolio').exists()

gestor_required = user_passes_test(is_gestor, login_url='/accounts/login/')

def portfolio_view(request):
    return render(request, 'portfoliopessoal/portfolio.html')

def sobre_view(request):
    try:
        portfolio = Projeto.objects.get(nomeProjeto="Portfolio Pessoal")
        tecnologias = portfolio.tecnologias.all().order_by('tipoTecnologia')
    except Projeto.DoesNotExist:
        tecnologias = []
    makingofs = MakingOf.objects.filter(projeto__nomeProjeto="Portfolio Pessoal").order_by('id')
    return render(request, 'portfoliopessoal/sobre.html', {
        'makingofs': makingofs,
        'tecnologias': tecnologias,
    })

def percurso_view(request):
    try:
        licenciatura = Licenciatura.objects.prefetch_related(
            'unidades_curriculares',
            'unidades_curriculares__equipa_docente',
        ).get(nomeCurso="Informática de Gestão")
    except Licenciatura.DoesNotExist:
        licenciatura = None
    formacoes = Formacao.objects.all().order_by('id')
    return render(request, 'portfoliopessoal/percurso.html', {
        'licenciatura': licenciatura,
        'formacoes': formacoes,
    })

def detalhe_docente_view(request, id):
    docente = get_object_or_404(
        Docente.objects.prefetch_related('ucs_lecionadas', 'tfcs_orientados'),
        idDocente=id
    )
    return render(request, 'portfoliopessoal/detalhe_docente.html', {'docente': docente})

@login_required(login_url='/accounts/login/')
@gestor_required
def admin_dashboard_view(request):
    return render(request, 'portfoliopessoal/admin_dashboard.html')

@login_required(login_url='/accounts/login/')
@gestor_required
def gestao_projetos_view(request):
    return render(request, 'portfoliopessoal/projetos.html', {
        'projetos': Projeto.objects.all(), 'gestao': True, 'is_gestor': True
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def gestao_competencias_view(request):
    return render(request, 'portfoliopessoal/competencias.html', {
        'competencias': Competencia.objects.all(), 'gestao': True, 'is_gestor': True
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def gestao_tecnologias_view(request):
    return render(request, 'portfoliopessoal/tecnologias.html', {
        'tecnologias': Tecnologia.objects.all(), 'gestao': True, 'is_gestor': True
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def gestao_formacoes_view(request):
    return render(request, 'portfoliopessoal/formacoes.html', {
        'formacoes': Formacao.objects.all(), 'gestao': True, 'is_gestor': True
    })

def projetos_view(request):
    gestor = is_gestor(request.user)
    return render(request, 'portfoliopessoal/projetos.html', {
        'projetos': Projeto.objects.all(),
        'is_gestor': gestor,
    })

def tecnologias_view(request):
    gestor = is_gestor(request.user)
    return render(request, 'portfoliopessoal/tecnologias.html', {
        'tecnologias': Tecnologia.objects.all(),
        'is_gestor': gestor,
    })

def licenciaturas_view(request):
    return render(request, 'portfoliopessoal/licenciaturas.html', {'licenciaturas': Licenciatura.objects.all()})

def ucs_view(request):
    return render(request, 'portfoliopessoal/ucs.html', {'ucs': UnidadeCurricular.objects.all()})

def tfcs_view(request):
    return render(request, 'portfoliopessoal/tfc.html', {'tfcs': TFC.objects.all()})

def docentes_view(request):
    return render(request, 'portfoliopessoal/docentes.html', {'docentes': Docente.objects.all()})

def competencias_view(request):
    gestor = is_gestor(request.user)
    return render(request, 'portfoliopessoal/competencias.html', {
        'competencias': Competencia.objects.all(),
        'is_gestor': gestor,
    })

def formacoes_view(request):
    gestor = is_gestor(request.user)
    return render(request, 'portfoliopessoal/formacoes.html', {
        'formacoes': Formacao.objects.all(),
        'is_gestor': gestor,
    })

def interesses_view(request):
    return render(request, 'portfoliopessoal/interesses.html', {'interesses': Interesse.objects.all()})

def makingof_view(request):
    dados = MakingOf.objects.select_related('projeto').all()
    return render(request, 'portfoliopessoal/makingof.html', {'logs': dados})

# CRUD: PROJETOS
@login_required(login_url='/accounts/login/')
@gestor_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gestao_projetos')
    return render(request, 'portfoliopessoal/projeto_form.html', {
        'form': form, 'titulo': 'Novo Projeto', 'cancel_url': 'gestao_projetos'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def editar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('gestao_projetos')
    return render(request, 'portfoliopessoal/projeto_form.html', {
        'form': form, 'titulo': 'Editar Projeto', 'cancel_url': 'gestao_projetos'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def apagar_projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('gestao_projetos')
    return render(request, 'portfoliopessoal/projeto_confirmar_delete.html', {
        'projeto': projeto, 'cancel_url': 'gestao_projetos'
    })

# CRUD: TECNOLOGIAS
@login_required(login_url='/accounts/login/')
@gestor_required
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gestao_tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_form.html', {
        'form': form, 'titulo': 'Nova Tecnologia', 'cancel_url': 'gestao_tecnologias'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def editar_tecnologia_view(request, nome):
    tecnologia = get_object_or_404(Tecnologia, nomeTecnologia=nome)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('gestao_tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_form.html', {
        'form': form, 'titulo': 'Editar Tecnologia', 'cancel_url': 'gestao_tecnologias'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def apagar_tecnologia_view(request, nome):
    tecnologia = get_object_or_404(Tecnologia, nomeTecnologia=nome)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('gestao_tecnologias')
    return render(request, 'portfoliopessoal/tecnologia_confirmar_delete.html', {
        'tecnologia': tecnologia, 'cancel_url': 'gestao_tecnologias'
    })

# CRUD: COMPETÊNCIAS
@login_required(login_url='/accounts/login/')
@gestor_required
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestao_competencias')
    return render(request, 'portfoliopessoal/competencias_form.html', {
        'form': form, 'titulo': 'Nova Competência', 'cancel_url': 'gestao_competencias'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def editar_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('gestao_competencias')
    return render(request, 'portfoliopessoal/competencias_form.html', {
        'form': form, 'titulo': 'Editar Competência', 'cancel_url': 'gestao_competencias'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def apagar_competencia_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('gestao_competencias')
    return render(request, 'portfoliopessoal/competencias_confirmar_delete.html', {
        'competencia': competencia, 'cancel_url': 'gestao_competencias'
    })

# CRUD: FORMAÇÃO
@login_required(login_url='/accounts/login/')
@gestor_required
def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestao_formacoes')
    return render(request, 'portfoliopessoal/formacoes_form.html', {
        'form': form, 'titulo': 'Nova Formação', 'cancel_url': 'gestao_formacoes'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def editar_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('gestao_formacoes')
    return render(request, 'portfoliopessoal/formacoes_form.html', {
        'form': form, 'titulo': 'Editar Formação', 'cancel_url': 'gestao_formacoes'
    })

@login_required(login_url='/accounts/login/')
@gestor_required
def apagar_formacao_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('gestao_formacoes')
    return render(request, 'portfoliopessoal/formacoes_confirmar_delete.html', {
        'formacao': formacao, 'cancel_url': 'gestao_formacoes'
    })