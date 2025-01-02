from django import forms
from .models import MedicationCard, DAYS

class MedicationCardForm(forms.ModelForm):
    """
    Form for adding or editing the medication
    """
    class Meta:
        """
        **Model**: :model:`MedicationCard`
        """
        model = MedicationCard
        fields = ('name', 'days', 'time', 'doses_per_day', 'interval_between_doses')

        labels = {
            'interval_between_doses': 'Interval between doses (hours)',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Medicine name'}),
            'time': forms.TimeInput(attrs={'type': 'time',}),
            'interval_between_doses': forms.NumberInput(attrs={'placeholder': '0',}),
        }

    days = forms.MultipleChoiceField(
        choices = DAYS,
        widget = forms.CheckboxSelectMultiple,
        required = True
    )


    def clean(self):
        """
        Validates and cleans the form data for the MedicationCard model.

        """
        cleaned_data = super().clean()
        doses_per_day = cleaned_data.get("doses_per_day")
        interval_between_doses = cleaned_data.get("interval_between_doses")

        if doses_per_day > 1 and not interval_between_doses:
            raise forms.ValidationError(
                "Please specify the interval between doses when doses  per day is more than 1."
            )

        if doses_per_day == 1:
            cleaned_data["interval_between_doses"] = None

        return cleaned_data
    
    