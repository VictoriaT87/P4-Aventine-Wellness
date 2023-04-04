from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    message = forms.CharField(required=True)
    
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )
