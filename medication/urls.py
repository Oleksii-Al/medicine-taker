from django.urls import path
from . import views

urlpatterns = [
    path('medication/', views.medication_list, name="medication")
]