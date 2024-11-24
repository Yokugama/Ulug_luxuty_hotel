from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import Hotel, Room, Booking
from .forms import BookingForm, SearchForm

def home(request):
    search_form = SearchForm()
    return render(request, 'hotels/home.html', {'search_form': search_form})

def hotel_list(request):
    hotels = Hotel.objects.all()
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        city = search_form.cleaned_data.get('city')
        check_in = search_form.cleaned_data.get('check_in')
        check_out = search_form.cleaned_data.get('check_out')
        guests = search_form.cleaned_data.get('guests')
        
        if city:
            hotels = hotels.filter(city__icontains=city)
        if check_in and check_out:
            hotels = hotels.filter(
                Q(rooms__booking__check_in_date__gte=check_out) |
                Q(rooms__booking__check_out_date__lte=check_in) |
                Q(rooms__booking__isnull=True)
            ).distinct()
        if guests:
            hotels = hotels.filter(rooms__capacity__gte=guests)
    
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels, 'search_form': search_form})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})

@login_required
def booking_create(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'hotels/booking_form.html', {'form': form, 'room': room})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'hotels/booking_confirmation.html', {'booking': booking})

@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hotels/profile.html', {'bookings': bookings})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'hotels/register.html', {'form': form})

