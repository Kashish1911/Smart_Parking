# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import ParkingSlot, Booking
from .forms import BookingForm

def index(request):
    # ensure some sample data exists (optional)
    if ParkingSlot.objects.count() == 0:
        rows = []
        for r in ['A', 'B']:
            for i in range(1, 7):
                rows.append(ParkingSlot(label=f"{r}{i}"))
        ParkingSlot.objects.bulk_create(rows)

    slots = ParkingSlot.objects.order_by('label')
    return render(request, 'myapp/index.html', {'slots': slots})


def slot_detail(request, id):
    slot = get_object_or_404(ParkingSlot, id=id)
    form = BookingForm()
    return render(request, 'myapp/slot_detail.html', {'slot': slot, 'form': form})


def book_slot(request, id):
    slot = get_object_or_404(ParkingSlot, id=id)
    if not slot.is_free:
        # simple redirect; you can flash messages via django.contrib.messages
        return redirect('home')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.slot = slot
            booking.save()
            slot.is_free = False
            slot.updated_at = timezone.now()
            slot.save()
            return redirect('bookings')
    return redirect('slot_detail', id=id)


def bookings(request):
    all_bookings = Booking.objects.order_by('-start_time')[:100]
    return render(request, 'myapp/bookings.html', {'bookings': all_bookings})


def admin_panel(request):
    slots = ParkingSlot.objects.order_by('label')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            label = request.POST.get('label')
            if label:
                ParkingSlot.objects.create(label=label)
        elif action == 'toggle':
            sid = request.POST.get('slot_id')
            s = get_object_or_404(ParkingSlot, id=sid)
            s.is_free = not s.is_free
            s.updated_at = timezone.now()
            s.save()
        elif action == 'remove':
            sid = request.POST.get('slot_id')
            s = get_object_or_404(ParkingSlot, id=sid)
            s.delete()
        return redirect('admin_panel')
    return render(request, 'myapp/admin_panel.html', {'slots': slots})


def api_slots(request):
    slots = ParkingSlot.objects.order_by('label').values('id', 'label', 'is_free', 'updated_at')
    # Django's JSON encoder will handle datetime if converted to string
    data = [{'id': s['id'], 'label': s['label'], 'is_free': s['is_free'], 'updated_at': s['updated_at'].isoformat() if s['updated_at'] else None} for s in slots]
    return JsonResponse(data, safe=False)
