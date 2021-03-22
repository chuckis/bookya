from django import forms
from .models import Book


class CheckboxSelectionForm(forms.Form):
    item = forms.CheckboxInput()

    def make_feed(self):
        # send email using the self.cleaned_data dictionary
        pass