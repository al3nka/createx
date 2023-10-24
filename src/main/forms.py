from django import forms
from main.models import DraftField


class UserCreatedFilterForm(forms.Form):
    show_user_drafts = forms.BooleanField(required=False, initial=False,
                                          widget=forms.CheckboxInput(attrs={'onChange': 'this.form.submit();',
                                                                               'class': 'form-check-input'}),
                                          label='Show only my template_drafts')


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Type some keyword...', 'style': 'min-width: 150px'}),
                                   label=None)
