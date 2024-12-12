from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.medication_add, name="medication_add"),
    path('medication/', views.medication_list, name="medication"),
]