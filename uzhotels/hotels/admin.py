from django.contrib import admin
from .models import Hotel, Room, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating')
    search_fields = ('name', 'city')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'price', 'capacity', 'available')
    list_filter = ('hotel', 'room_type', 'available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in_date', 'check_out_date', 'status')
    list_filter = ('status', 'check_in_date', 'check_out_date')
    search_fields = ('user__username', 'room__hotel__name')

