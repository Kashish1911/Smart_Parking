# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('slot/<int:id>/', views.slot_detail, name='slot_detail'),
    path('book/<int:id>/', views.book_slot, name='book_slot'),
    path('bookings/', views.bookings, name='bookings'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('api/slots/', views.api_slots, name='api_slots'),
]
