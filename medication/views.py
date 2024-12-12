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



# def medication_edit(requst, name, medication_id):

#     queryset = MedicationCard.objects.all()
#     medication = get_object_or_404(queryset, name=name)
#     medication_form = MedicationCardForm(data=request.POST, instance=medication)
    
#     if request.method == "POST" and medication_form.is_valid() and request.user == medication.user:
#         medication = medication_form.save(commit=False)
#         medication.save()
#         messages.add_message(
#             request, messages.SUCCESS,
#             "Medication Updated!"
#         )
#     else:
#         messages.add_message(
#             request, messages.ERROR,
#             "Error updating medication!"
#         )
#     return HttpRenponseRedirect(reverse("medication_detail", args=[name]))

