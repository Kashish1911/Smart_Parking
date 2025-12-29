# myapp/admin.py
from django.contrib import admin
from .models import ParkingSlot, Booking

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'is_free', 'updated_at')
    list_filter = ('is_free',)
    search_fields = ('label',)
    ordering = ('label',)
    list_editable = ('is_free',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'slot', 'user_name', 'vehicle_no', 'start_time', 'end_time')
    search_fields = ('user_name', 'vehicle_no', 'slot__label')
    list_filter = ('slot', 'start_time')
    ordering = ('-start_time',)
