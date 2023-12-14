from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PersonaForm, DireccionForm
from .models import Persona, Direccion
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })


@login_required
def persona(request):
    personas = Persona.objects.all()
    return render(request, 'persona.html', {
        'personas': personas
    })


@login_required
def direccion(request):
    direccions = Direccion.objects.all()
    return render(request, 'direccion.html', {
        'direccions': direccions
    })


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
def create_persona(request):
    if request.method == 'GET':
        return render(request, 'create_persona.html', {
            'form': PersonaForm
        })
    else:
        try:
            form = PersonaForm(request.POST)
            new_persona = form.save(commit=False)
            new_persona.save()
            return redirect('persona')
        except ValueError:
            return render(request, 'create_persona.html', {
                'form': PersonaForm,
                'error': 'Provee datos validos'
            })


@login_required
def create_direccion(request):
    if request.method == 'GET':
        return render(request, 'create_direccion.html', {
            'form': DireccionForm
        })
    else:
        try:
            form = DireccionForm(request.POST)
            new_direccion = form.save(commit=False)
            new_direccion.save()
            return redirect('direccion')
        except ValueError:
            return render(request, 'create_direccion.html', {
                'form': DireccionForm,
                'error': 'Provee datos validos'
            })


@login_required
def persona_detail(request, persona_id):
    if request.method == 'GET':
        persona = get_object_or_404(Persona, pk=persona_id)
        form = PersonaForm(instance=persona)
        return render(request, 'persona_detail.html', {'persona': persona, 'form': form})
    else:
        try:
            persona = get_object_or_404(Persona, pk=persona_id)
            form = PersonaForm(request.POST, instance=persona)
            form.save()
            return redirect('persona')
        except ValueError:
            return render(request, 'persona_detail.html', {'persona': persona, 'form': form,
                                                           'error': 'error updating persona'})


@login_required
def direccion_detail(request, direccion_id):
    if request.method == 'GET':
        direccion = get_object_or_404(Direccion, pk=direccion_id)
        form = DireccionForm(instance=direccion)
        return render(request, 'direccion_detail.html', {'direccion': direccion, 'form': form})
    else:
        try:
            direccion = get_object_or_404(Direccion, pk=direccion_id)
            form = DireccionForm(request.POST, instance=direccion)
            form.save()
            return redirect('direccion')
        except ValueError:
            return render(request, 'direccion_detail.html', {'direccion': direccion, 'form': form,
                                                             'error': 'error updating persona'})


@login_required
def delete_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona')


@login_required
def delete_direccion(request, direccion_id):
    direccion = get_object_or_404(Direccion, pk=direccion_id)
    if request.method == 'POST':
        direccion.delete()
        return redirect('direccion')
