from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm

def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()

def lista_artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    autor = is_autor(request.user)
    return render(request, 'artigos/lista_artigos.html', {
        'artigos': artigos,
        'is_autor': autor,
    })

def detalhe_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all().order_by('data_criacao')
    form_comentario = ComentarioForm()
    autor = is_autor(request.user)

    if request.method == 'POST' and request.user.is_authenticated:
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            comentario = form_comentario.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('detalhe_artigo', id=id)

    return render(request, 'artigos/detalhe_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'is_autor': autor,
    })

@login_required(login_url='/accounts/login/')
def novo_artigo_view(request):
    if not is_autor(request.user):
        return redirect('lista_artigos')
    form = ArtigoForm()
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('lista_artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required(login_url='/accounts/login/')
def editar_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('lista_artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('detalhe_artigo', id=id)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo'})

@login_required(login_url='/accounts/login/')
def apagar_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('lista_artigos')
    if request.method == 'POST':
        artigo.delete()
        return redirect('lista_artigos')
    return render(request, 'artigos/artigo_confirmar_delete.html', {'artigo': artigo})

def like_artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key
    like, criado = Like.objects.get_or_create(artigo=artigo, sessao=sessao)
    if not criado:
        like.delete()
    return redirect('detalhe_artigo', id=id)