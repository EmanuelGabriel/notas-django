from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Criando minhas 'Views' aqui.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            aux_user = User.objects.get(username=email)

            if aux_user:
                found_user = authenticate(username=email,
                                          password=password)
                if found_user is not None:
                    login(request, found_user)
                    return HttpResponseRedirect('/home/')

        except User.DoesNotExist:
            return render(request, 'site/index.html', {'message': 'Usuário não cadastrado!'})

    return render(request, 'site/index.html')


def cadastroUsuario(request):
    return render(request, 'site/cadastro-usuario.html')


def sobre(request):
    return render(request, 'site/sobre.html')


def registro(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            aux_user = User.objects.get(username=email)

            if aux_user:
                return render(request, 'site/register.html', {'message': 'Este e-mail já está registrado.'})

        except User.DoesNotExist:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.save()
            return render(request, 'site/register.html', {'message': 'Conta criada com sucesso!'})

    return render(request, 'site/register.html')


@login_required
def home(request):
    user = request.user
    notes_this_user = Note.objects.filter(author=user).order_by('-date_created')
    return render(request, 'site/home.html', {'notes': notes_this_user})


@login_required
def create_note(request):
    form = NoteForm

    if request.POST:
        data = {
            'author': request.user.id,
            'title': request.POST['title'],
            'content': request.POST['content'],
            'color': request.POST['color']
        }
        new_note = NoteForm(data)
        if new_note.is_valid():
            new_note.save(data)

        return HttpResponseRedirect("/home/")

    return render(request, 'site/create-note.html', {'form': form})


@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, pk=id)
    form = NoteForm(request.POST or None, instance=note)

    if request.POST:
        data = {
            'author': request.user.id,
            'title': request.POST['title'],
            'content': request.POST['content'],
            'color': request.POST['color']
        }
        form = NoteForm(data, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")

    return render(request, 'site/edit-note.html', {'form': form, 'note': note})


@require_POST
@login_required
def delete_note(request, id):
    note = Note.objects.filter(id=id).delete()
    return HttpResponseRedirect("/home/")


@require_POST
@login_required
def exit(request):
    logout(request)
    return HttpResponseRedirect('/')
