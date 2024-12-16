from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

DAYS = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday")
    )

class MedicationCard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medications"
    )
    name = models.CharField(max_length=200)
    days = models.JSONField()
    time = models.TimeField()
    doses_per_day = models.PositiveIntegerField(default = 1)
    interval_between_doses = models.PositiveIntegerField(blank = True, null = True, default = None)
    photo = CloudinaryField('image', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['user', 'name'], name='unique_medication_for_user')
        ]


    def __str__(self):
        return f"{self.name} (ID:{self.id})"

class MedicationSchedule(models.Model):
    medication = models.ForeignKey(
        MedicationCard, on_delete=CASCADE, related_name='schedules'
    )
    day_of_week = models.CharField(max_length=9, choices=DAYS)
    time = models.TimeField()
    status = models.BooleanField(default = False) #False - medication isn't taken / True - is taken
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medication.name} on {self.day_of_week} at {self.time}"