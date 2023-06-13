from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PostForm
# Create your views here
from .models import Post
from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime
from .models import Post, Comentario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def home_page_view(request):

    local = 'Lisboa'

    context = {
        'ano': datetime.now().year,
        'local': local,
        'Post': Post.objects.all(),
    }


    return render(request, 'portfolio/home.html', context)


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def nova_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))


    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)

@login_required
def editar_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/edita.html', context)
@login_required
def apaga_page_view(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('home'))


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)

            login(request, user)
            return redirect('home')

        else:
            message = 'As senhas não correspondem.'



        return HttpResponseRedirect(reverse('home'))