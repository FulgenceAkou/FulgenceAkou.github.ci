from django.core import validators
from django import forms
from .models import User

class ParticipantResgistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prénom', 'numéro', 'adresse_email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control'}),
            'numéro': forms.NumberInput(attrs={'class': 'form-control'}),
            'adresse_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }