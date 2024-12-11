from django import forms
from .models import MedicationCard, DAYS

class MedicationCardForm(forms.ModelForm):
    class Meta:
        model = MedicationCard
        fields = ('name', 'user', 'days', 'time', 'doses_per_day', )

    days = forms.MultipleChoiceField(
        choices = DAYS,
        widget = forms.CheckboxSelectMultiple,
        required = True
    )