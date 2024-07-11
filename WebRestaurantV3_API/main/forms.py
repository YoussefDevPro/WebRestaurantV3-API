from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'id': 'phone', 'name': 'phone'}),
            'date': forms.DateInput(attrs={'type': 'date', 'id': 'date', 'name': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'id': 'time', 'name': 'time'}),
            'guests': forms.NumberInput(attrs={'type': 'number', 'id': 'guests', 'name': 'guests'}),
        }


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    order_date = forms.DateField()
    burgers = forms.ModelMultipleChoiceField(queryset=Burger.objects.all(), required=False)
    desserts = forms.ModelMultipleChoiceField(queryset=Dessert.objects.all(), required=False)
    pizzas = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), required=False)
    plats = forms.ModelMultipleChoiceField(queryset=Plat.objects.all(), required=False)
    sandwiches = forms.ModelMultipleChoiceField(queryset=Sandwich.objects.all(), required=False)
    supplements = forms.ModelMultipleChoiceField(queryset=Supplement.objects.all(), required=False)
    tacos = forms.ModelMultipleChoiceField(queryset=Tacos.objects.all(), required=False)
