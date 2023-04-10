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
                'style': "width:100%; height:40px;",
                'placeholder': "Email"
                }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;",
                'placeholder': "Full Name"
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;",
                'placeholder': "Title of Your Business Enquiry"
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'style': "width:100%; height:150px;",
                'placeholder': "Message"
                }),
        }
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ('date_created', 'date_updated', 'author' )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width:100%; height:40px;"
                }),
        }
