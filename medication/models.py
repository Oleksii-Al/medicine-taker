from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

DAYS = (("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"))

class MedicationCard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_medication"
    )
    name = models.CharField(max_length=200)
    days = models.JSONField()
    time = models.TimeField()
    doses_per_day = models.PositiveIntegerField(default = 1)
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

