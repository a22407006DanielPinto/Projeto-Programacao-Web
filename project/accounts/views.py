from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings
import secrets
from .forms import RegistoForm
from .models import MagicToken

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            erro = 'Credenciais inválidas. Tenta novamente.'
    return render(request, 'accounts/login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('/')

def registo_view(request):
    form = RegistoForm()
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_autores, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/registo.html', {'form': form})

def magic_link_view(request):
    mensagem = None
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = secrets.token_urlsafe(32)
            MagicToken.objects.update_or_create(user=user, defaults={'token': token})
            link = f"{settings.SITE_URL}/accounts/autenticar/?token={token}"
            send_mail(
                subject='Portfolio — Link de Autenticação',
                message=f'Olá {user.username},\n\nClica no link abaixo para entrar:\n\n{link}\n\nO link é de uso único.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            mensagem = 'Email enviado! Verifica a tua caixa de entrada.'
        except User.DoesNotExist:
            erro = 'Não existe nenhuma conta com esse email.'
    return render(request, 'accounts/magic_link.html', {'mensagem': mensagem, 'erro': erro})

def autenticar_token_view(request):
    token = request.GET.get('token')
    try:
        magic = MagicToken.objects.get(token=token)
        user = magic.user
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        magic.delete()
        return redirect('/')
    except MagicToken.DoesNotExist:
        return render(request, 'accounts/token_invalido.html')