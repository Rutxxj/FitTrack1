from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import WeightMeasurement,Food,UserProfile
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class WeightMeasurementForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter date mm/dd/yyyy'}))
    
    class Meta:
        model = WeightMeasurement
        fields = ['date', 'weight']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['id','food_name','quantity', 'calories', 'fat', 'carbohydrates', 'protein']

class BMRForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['age','weight','height','gender']

