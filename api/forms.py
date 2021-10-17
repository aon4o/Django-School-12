from django import forms


class LimitForms(forms.Form):
    limit = forms.DecimalField(
        widget=forms.NumberInput(attrs={'step': 10, 'value': 10}),
        label='Records per page',
        min_value=10,
        max_value=100,
    )
