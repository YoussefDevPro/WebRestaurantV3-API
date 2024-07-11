from django.contrib import admin
from .models import *


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'guests')


class BurgerAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'prix_XXL', 'vegetarienne', 'disponibilite', 'image_link')


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix_petite', 'prix', 'prix_grand', 'vegetarienne', 'disponibilite', 'image_link')


class TacosAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'prix_XXL', 'vegetarienne', 'disponibilite', 'image_link')


class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'vegetarienne', 'disponibilite', 'image_link')


class SandwichAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'prix_XXL', 'vegetarienne', 'disponibilite', 'image_link')


class DessertAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'disponibilite', 'image_link')


class SupplementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'disponibilite', 'image_link')


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email", "order_date", "ordered_products", "total")


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Supplement, SupplementAdmin)
admin.site.register(Burger, BurgerAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Tacos, TacosAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Sandwich, SandwichAdmin)
admin.site.register(Plat, PlatAdmin)
admin.site.register(Order, OrderAdmin)
