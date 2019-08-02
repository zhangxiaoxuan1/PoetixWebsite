from django import forms

class PoemForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=50)
