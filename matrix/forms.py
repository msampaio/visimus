import re
from django import forms

class RowForm(forms.Form):
    row = forms.CharField(max_length=60,
                          widget=forms.TextInput(attrs={'data-regex':"^[0-9 ]+$"}))
    notes = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'data-regex':"^[0-9 ]+$"}))

    def clean_row(self):
        row = self.cleaned_data['row']
        if not re.search(r'^[\d ]+$', row):
            raise forms.ValidationError("A row can contain only digits.")
        else:
            return row

    def clean_notes(self):
        notes = self.cleaned_data['notes']
        if not re.search(r'^[\d ]+$', notes):
            raise forms.ValidationError("The notes must be entered as digits.")
        else:
            return notes
