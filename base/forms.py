from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ('package', )
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;"
                }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;"
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;"
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'style': "width:100%; height:150px;"
                }),
        }
