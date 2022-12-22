from django import forms
from django.forms import CharField, SelectDateWidget, DateInput, DateField
from SEMINARIO.models import Participantes



class ParticipantesForm(forms.ModelForm):
    class Meta:
        model = Participantes
        fields = '__all__'
