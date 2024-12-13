from django.contrib import admin
from .models import MedicationCard, MedicationSchedule
from .forms import MedicationCardForm

# Register your models here.
class MedicationCardAdmin(admin.ModelAdmin):
    form = MedicationCardForm

    list_display = ('name', 'user', 'days', 'time', 'doses_per_day', 'interval_between_doses')
    search_fields = ('name',)

class MedicationScheduleAdmin(admin.ModelAdmin):
    list_display = ('medication', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields =('medication', 'status')



admin.site.register(MedicationCard, MedicationCardAdmin)
admin.site.register(MedicationSchedule)