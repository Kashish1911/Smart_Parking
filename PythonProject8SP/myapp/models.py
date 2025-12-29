# myapp/models.py
from django.db import models
from django.utils import timezone

class ParkingSlot(models.Model):
    label = models.CharField(max_length=20, unique=True)
    is_free = models.BooleanField(default=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.label


class Booking(models.Model):
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.slot.label} — {self.user_name}"
