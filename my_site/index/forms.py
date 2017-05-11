from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message is None:
            raise forms.ValidationError('Please enter a message.')

        return message

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name is None:
            raise forms.ValidationError('Please enter your name.')

        return name

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()

        return cleaned_data

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

