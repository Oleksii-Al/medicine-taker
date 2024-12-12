from django import forms
from .models import MedicationCard, DAYS

class MedicationCardForm(forms.ModelForm):
    class Meta:
        model = MedicationCard
        fields = ('name', 'user', 'days', 'time', 'doses_per_day', 'interval_between_doses')

    days = forms.MultipleChoiceField(
        choices = DAYS,
        widget = forms.CheckboxSelectMultiple,
        required = True
    )

    def clean(self):
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