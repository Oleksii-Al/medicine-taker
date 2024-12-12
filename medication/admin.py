from django.contrib import admin
from .models import MedicationCard
from .forms import MedicationCardForm

# Register your models here.
class MedicationCardAdmin(admin.ModelAdmin):
    form = MedicationCardForm

    list_display = ('name', 'user', 'days', 'time', 'doses_per_day', 'interval_between_doses')
    search_fields = ('name',)

admin.site.register(MedicationCard, MedicationCardAdmin)