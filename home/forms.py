from django import forms
from .models import Contact

from http import HTTPStatus


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 5}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )
