from django.forms import ModelForm
from .models import *


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido_p', 'apellido_m']

