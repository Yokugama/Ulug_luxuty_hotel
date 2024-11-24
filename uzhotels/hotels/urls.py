from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('booking/<int:room_id>/', views.booking_create, name='booking_create'),
    path('booking/<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]

