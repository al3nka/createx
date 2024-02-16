from django import forms


class DraftTextField(forms.CharField):
    def __init__(self, label, help_text, html_id):
        self.required = True
        self.label = label
        self.max_length = 100
        attrs = {
            'class': 'form-control',
            'id': html_id,
        }
        if help_text:
            attrs['placeholder'] = help_text

        self.widget = forms.TextInput(attrs=attrs)
        super(DraftTextField, self).__init__(
            max_length=self.max_length
        )
        self.help_text = help_text


class DraftParagraphField(forms.CharField):
    def __init__(self, label, help_text, html_id):
        self.required = True
        self.label = label
        self.max_length = 1000
        super(DraftParagraphField, self).__init__(
            max_length=self.max_length
        )
        attrs = {
            'class': 'form-control',
            'id': html_id,
            'rows': 3,
        }
        if help_text:
            attrs['placeholder'] = help_text
        self.widget = forms.Textarea(attrs=attrs)


class DraftNumberField(forms.FloatField):
    def __init__(self, label, help_text, html_id):
        self.required = True
        self.label = label
        super(DraftNumberField, self).__init__()
        attrs = {
            'class': 'form-control',
            'id': html_id,
        }
        if help_text:
            attrs['placeholder'] = help_text
        self.widget = forms.NumberInput(attrs=attrs)


class DraftBooleanField(forms.BooleanField):
    def __init__(self, label, help_text, html_id):
        self.required = True
        self.label = label
        self.help_text = help_text
        super(DraftBooleanField, self).__init__()
        attrs = {
            'class': 'form-check-input',
            'id': html_id,
        }
        if help_text:
            attrs['placeholder'] = help_text
        self.widget = forms.CheckboxInput(attrs=attrs)


class DraftDateField(forms.DateField):
    def __init__(self, label, help_text, html_id):
        self.required = True
        self.label = label
        super(DraftDateField, self).__init__()
        attrs = {
            'class': 'form-control',
            'id': html_id,
            'type': 'date'
        }
        if help_text:
            attrs['placeholder'] = help_text
        self.widget = forms.DateInput(format='%d-%m-%Y', attrs=attrs)