from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MedicationCard
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