from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PersonaForm
from .models import Persona


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


def persona(request):
    personas = Persona.objects.all()
    return render(request, 'persona.html', {
        'personas': personas
    })


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


def delete_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona')
