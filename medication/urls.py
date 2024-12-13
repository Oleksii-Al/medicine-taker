from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.medication_add, name="medication_add"),
    path('delete/<int:medication_id>/', views.medication_delete, name='medication_delete'),
    path('edit/<int:medication_id>/', views.medication_edit, name="medication_edit"),
    path('', views.medication_week, name="medication"),
]