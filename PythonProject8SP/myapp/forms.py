from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot', 'user_name', 'vehicle_no', 'start_time', 'end_time']
        # Or simply:
        # fields = '__all__'
