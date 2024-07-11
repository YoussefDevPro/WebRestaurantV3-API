from django.db import models
from django.utils import timezone



class Reservation(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f'Reservation for {self.name} on {self.date} at {self.time}'


class Burger(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix = models.FloatField(default=0)
    prix_XXL = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Dessert(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix = models.FloatField(default=0)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Pizza(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix_petite = models.FloatField(default=0)
    prix = models.FloatField(default=0)
    prix_grand = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Plat(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Sandwich(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix = models.FloatField(default=0)
    prix_XXL = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Supplement(models.Model):
    nom = models.CharField(max_length=500)
    prix = models.FloatField(default=0)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Tacos(models.Model):
    nom = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=5000)
    prix = models.FloatField(default=0)
    prix_XXL = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    disponibilite = models.BooleanField(default=True)
    image_link = models.CharField(max_length=10000)

    def __str__(self):
        return self.nom

    @property
    def class_name(self):
        return self.__class__.__name__


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now_add=True)  # Date and time when the order was created
    ordered_products = models.TextField()  # saved as JSON
    total = models.FloatField()

    def __str__(self):
        return f'Order by {self.name} on {self.order_date.strftime("%Y-%m-%d %H:%M:%S")}'


