from django import forms
from .models import Booking

class SearchForm(forms.Form):
    city = forms.CharField(required=False)
    check_in = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField(required=False, min_value=1)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'guests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

