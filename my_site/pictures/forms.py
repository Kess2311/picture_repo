from django import forms
from .models import Picture


class PictureForm(forms.ModelForm):

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description is None:
            raise forms.ValidationError('Please enter a Description.')

        return description

    def clean(self):
        cleaned_data = super(PictureForm, self).clean()

        return cleaned_data

    class Meta:
        model = Picture
        fields = ['file', 'description', 'location', 'date']

