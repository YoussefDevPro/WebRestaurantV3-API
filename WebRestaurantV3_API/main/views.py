from django.http import JsonResponse
from django.shortcuts import *
from .models import *
from .forms import *
from .forms import *
import json
from django.core import serializers


def index(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'main/index.html', {'form': form})


def menu(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'main/menu.html', {'form': form})


def pizza(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    pizzas = Pizza.objects.filter(disponibilite=True)
    return render(request, 'main/pizza.html', {'form': form, 'pizzas': pizzas})


def tacos(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    tacoss = Tacos.objects.filter(disponibilite=True)
    return render(request, 'main/tacos.html', {'form': form, 'tacos': tacoss})


def burger(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    burgers = Burger.objects.filter(disponibilite=True)
    return render(request, 'main/burger.html', {'form': form, 'burgers': burgers})


def plat(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    plats = Plat.objects.filter(disponibilite=True)
    return render(request, 'main/plat.html', {'form': form, 'plats': plats})


def sandwich(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    sandwichs = Sandwich.objects.filter(disponibilite=True)
    return render(request, 'main/sandwich.html', {'form': form, 'sandwichs': sandwichs})


def dessert(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    desserts = Dessert.objects.all()
    return render(request, 'main/dessert.html', {'form': form, 'desserts': desserts})


def get_all_products():
    products = []
    for model in [Burger, Dessert, Pizza, Plat, Sandwich, Supplement, Tacos]:
        products += list(model.objects.filter(disponibilite=True))
    return products


def order_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        order_date = request.POST.get('order_date')
        ordered_products = json.loads(request.POST.get('ordered_products'))
        order_total = float(request.POST.get('order_total'))

        # Save the order
        order = Order.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            order_date=order_date,
            ordered_products=json.dumps(ordered_products),
            total=order_total
        )

        return render(request=request, template_name='main/order_success.html', context={'totale': order_total})

    context = {
        'burgers': Burger.objects.filter(disponibilite=True),
        'desserts': Dessert.objects.filter(disponibilite=True),
        'pizzas': Pizza.objects.filter(disponibilite=True),
        'plats': Plat.objects.filter(disponibilite=True),
        'sandwiches': Sandwich.objects.filter(disponibilite=True),
        'tacos': Tacos.objects.filter(disponibilite=True),
    }
    return render(request, 'main/order_form.html', context)

def reserve_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'main/reserve.html', {'form': form})


def api_get_all_json_data(request):
    items_order = Order.objects.all()
    items_reservation = Reservation.objects.all()

    data = {
        'order': list(items_order.values()),
        'reservation': list(items_reservation.values()),
    }

    return JsonResponse(data, safe=False)


