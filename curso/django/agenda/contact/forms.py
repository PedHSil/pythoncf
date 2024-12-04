from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nome', 
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Sobrenome',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefone',
                    'class': 'form-control',
                }
            ),
        }
        
    def clean(self):
        #cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()