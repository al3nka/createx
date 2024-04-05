from typing import Iterable

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from main.models import DraftField, DraftFieldType, user_model
from main.fields import DraftTextField, DraftParagraphField, DraftBooleanField, DraftDateField, DraftNumberField


class UserCreatedFilterForm(forms.Form):
    show_user_drafts = forms.BooleanField(required=False, initial=False,
                                          widget=forms.CheckboxInput(attrs={'onChange': 'this.form.submit();',
                                                                            'class': 'form-check-input'}),
                                          label='Show only my tex drafts')


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('Type some keyword...'), 'style': 'min-width: 150px'}),
                                   label=None)


class DraftFieldFillForm(forms.Form):
    def create_field(self, draft_field: DraftField):
        field_type = {
            DraftFieldType.NUMBER: DraftNumberField,
            DraftFieldType.TEXT: DraftTextField,
            DraftFieldType.PARAGRAPH: DraftParagraphField,
            DraftFieldType.BOOL: DraftBooleanField,
            DraftFieldType.DATE: DraftDateField
        }
        self.fields[draft_field.jinja_variable] = field_type[draft_field.field_type](
            draft_field.name,
            draft_field.help_text,
            draft_field.jinja_variable
        )

    def __init__(self, draft_fields: Iterable[DraftField], *args, **kwargs):
        # template_fields = kwargs.pop('fields')
        super().__init__(*args, **kwargs)

        for draft_field in draft_fields:
            self.create_field(draft_field)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = user_model
        fields = ['username', 'email', 'password1', 'password2']
