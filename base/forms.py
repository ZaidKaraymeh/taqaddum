from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ('package', )

        def __init__(self, *args, **kwargs):
            self.fields['email'].widget.attrs['style'] = 'width:100%; height:40px;'
            self.fields['full_name'].widget.attrs['style'] = 'width:100%; height:40px;'
            self.fields['title'].widget.attrs['style'] = 'width:100%; height:40px;'
            self.fields['message'].widget.attrs['style'] = 'width:100%; height:200px;'
            self.fields['homework'].widget.attrs['style'] = 'width:100%; height:40px;'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['full_name'].widget.attrs['class'] = 'form-control'
            self.fields['title'].widget.attrs['class'] = 'form-control'
            self.fields['message'].widget.attrs['class'] = 'form-control'
            self.fields['homework'].widget.attrs['class'] = 'form-control'