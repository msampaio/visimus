from django import forms


class RowForm(forms.Form):
    row = forms.CharField(max_length=60)
    notes = forms.CharField(max_length=100)
