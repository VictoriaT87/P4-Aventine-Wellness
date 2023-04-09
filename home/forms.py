from django import forms
from .models import Contact

from http import HTTPStatus


class ContactForm(forms.ModelForm):
    name = forms.CharField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")

        return cleaned_data
