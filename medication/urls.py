from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.medication_add, name="medication_add"),
    path('edit/<int:medication_id>/', views.medication_edit, name="medication_edit"),
    path('medication/', views.medication_list, name="medication"),
]