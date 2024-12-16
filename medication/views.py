from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MedicationCard, MedicationSchedule, DAYS
from .forms import MedicationCardForm

# Create your views here.
@login_required
def medication_list(request):
    medications = MedicationCard.objects.filter(user=request.user)
    return render(
        request,
        "medication/medication_list.html",
        {
            "medications": medications,
        },
    )

@login_required
def medication_add(request):

    if request.method == "POST":
        medication_form = MedicationCardForm(request.POST)
        if medication_form.is_valid():
            medication = medication_form.save(commit=False)
            medication.user = request.user
            medication.save()
            
            for day in medication.days:
                MedicationSchedule.objects.create(
                    medication = medication,
                    day_of_week = day,
                    time = medication.time,
                    status = False,
                )

            messages.success(
                request, "Medication is added"
            )

            return redirect('medication')
    else:
        medication_form = MedicationCardForm()

    return render(
        request,
        "medication/medication_add.html",
        {
            "medication_form": medication_form,
        }
        )


@login_required
def medication_edit(request, medication_id):

    medication = get_object_or_404(MedicationCard, pk=medication_id)

    if medication.user != request.user:
        messages.error(
            request, "You don't have permission to edit this medication."
        )
        return redirect("medication")

    if request.method == "POST":
        medication_form = MedicationCardForm(request.POST, instance=medication)
        if medication_form.is_valid():
            medication_form.save()
            messages.success(request, "Medication updated successfully!")
            return redirect("medication")
    else:
        medication_form = MedicationCardForm(instance=medication)


    return render(
        request,
        "medication/medication_edit.html",
        {
            "medication_form": medication_form,
        }
    )

@login_required
def medication_delete(request, medication_id):

    medication = get_object_or_404(MedicationCard, pk=medication_id)

    if medication.user == request.user:
        medication.delete()
        messages.success(request, "Medication deleted!")
        return redirect("medication")

    else:
        messages.error(
            request, "You don't have permission to delete this medication."
        )
        return redirect("medication")

@login_required
def medication_week(request):
    medications = MedicationCard.objects.filter(user = request.user)
    schedules = MedicationSchedule.objects.filter(medication__in=medications)

    schedule = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    for schedule_item in schedules:
        schedule[schedule_item.day_of_week].append(schedule_item)

    for day in schedule:
           schedule[day] = sorted(schedule[day], key=lambda item: item.time)
    
    return render(
        request,
        "medication/schedule.html",
        {
            "schedule": schedule,
        }
    )
                 
@login_required
def medication_take(request, schedule_id):

    schedule = get_object_or_404(MedicationSchedule, pk=schedule_id)

    if schedule.medication.user == request.user:
        schedule.status = not schedule.status
        schedule.save()
        messages.success(
            request, "The status is updated"
        )

    else:
        messages.error(
            request, "You don't have permission to change the status of this medication."
        )
    
    return redirect('medication')