from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
import requests
import json

url = 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data'


class MainWidget(TabbedPanel):
    pass

class CustomBoxLayout(BoxLayout):
    def __init__(self, bg_color=(0.3, 0.3, 0.3, 1), **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class OrderView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = StackLayout(orientation='lr-tb', padding=10, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.add_widget(self.layout)
        self.load_orders()

    def load_orders(self):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            orders = data.get('order', [])
            if orders:
                for order_details in orders:
                    order_id = order_details['id']
                    order_name = order_details['name']
                    order_phone = order_details['phone']
                    order_email = order_details['email']
                    order_address = order_details['address']
                    order_date = order_details['order_date']
                    ordered_products = json.loads(order_details['ordered_products'])
                    totale = order_details['total']
                    item = OrderItem(order_id, order_name, order_phone, order_email, order_address, order_date,
                                     ordered_products, totale)
                    self.layout.add_widget(item)
            else:
                print("No orders found")  # Debugging line
        except Exception as e:
            print("Error loading orders:", e)  # Debugging line


class OrderItem(StackLayout):
    numero_de_commande = StringProperty()
    order_name = StringProperty()
    order_phone = StringProperty()
    order_email = StringProperty()
    order_address = StringProperty()
    order_date = StringProperty()
    totale_str = StringProperty()

    def __init__(self, numero_de_commande, order_name, order_phone, order_email, order_address, order_date,
                 ordered_products, totale, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        self.padding = 10
        self.spacing = 20
        self.size_hint_y = None
        self.height = self.minimum_height

        self.numero_de_commande = "#" + str(numero_de_commande)
        self.order_name = str(order_name)
        self.order_phone = str(order_phone)
        self.order_email = str(order_email)
        self.order_address = str(order_address)
        self.order_date = str(order_date)
        self.totale_str = f"{totale} DH"

        self.add_widget(self.create_label_pair("Facture de commande", self.numero_de_commande))
        self.add_widget(self.create_label_pair("Nom du client:", self.order_name))
        self.add_widget(self.create_label_pair("Téléphone:", self.order_phone))
        self.add_widget(self.create_label_pair("Email:", self.order_email))
        self.add_widget(self.create_label_pair("Adresse:", self.order_address))
        self.add_widget(self.create_label_pair("Date de la commande:", self.order_date))

        self.add_widget(self.create_label("Produits commandés:"))
        for product in ordered_products:
            product_name = str(product['name'])
            product_price = str(product['price']) + " DH"
            self.add_widget(self.create_label_pair(product_name, product_price))

        self.add_widget(self.create_label_pair("Totale payé", self.totale_str))

    def create_label_pair(self, text1, text2):
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text1, size_hint=(0.4, None), height=30, bold=True, halign='right'))
        layout.add_widget(Label(text=text2, size_hint=(0.6, None), height=30, halign='right'))
        layout_.add_widget(layout)
        return layout_

    def create_label(self, text):
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text, size_hint=(1.0, None), height=30, bold=True, halign='right'))
        layout_.add_widget(layout)
        return layout_


class ReservationView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = StackLayout(orientation='lr-tb', padding=10, spacing=30, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.add_widget(self.layout)
        self.load_reservations()

    def load_reservations(self):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            reservations = data.get('reservation', [])
            if reservations:
                for reservation_details in reservations:
                    reservation_id = reservation_details['id']
                    reservation_name = reservation_details['name']
                    reservation_phone = reservation_details['phone']
                    reservation_email = reservation_details['email']
                    reservation_date = reservation_details['date']
                    reservation_time = reservation_details['time']
                    reservation_guests = reservation_details['guests']
                    item = ReservationItem(reservation_id, reservation_name, reservation_phone, reservation_email,
                                           reservation_date, reservation_time, reservation_guests)
                    self.layout.add_widget(item)
            else:
                print("No reservations found")  # Debugging line
        except Exception as e:
            print("Error loading reservations:", e)  # Debugging line


class ReservationItem(StackLayout):
    id = StringProperty()
    nom = StringProperty()
    phone = StringProperty()
    email = StringProperty()
    date = StringProperty()
    hour = StringProperty()
    nb_invited = StringProperty()

    def __init__(self, id, nom, phone, email, date, hour, nb_invited, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        self.padding = 10
        self.spacing = 20
        self.size_hint_y = None
        self.height = self.minimum_height

        self.id = "#" + str(id)
        self.nom = str(nom)
        self.phone = str(phone)
        self.email = str(email)
        self.date = str(date)
        self.hour = str(hour)
        self.nb_invited = str(nb_invited)

        self.add_widget(self.create_label_pair("Réservation", self.id))
        self.add_widget(self.create_label_pair("Nom:", self.nom))
        self.add_widget(self.create_label_pair("Téléphone:", self.phone))
        self.add_widget(self.create_label_pair("Email:", self.email))
        self.add_widget(self.create_label_pair("Date:", self.date))
        self.add_widget(self.create_label_pair("Heure:", self.hour))
        self.add_widget(self.create_label_pair("Nombre de convives:", self.nb_invited))

    def create_label_pair(self, text1, text2):
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text1, size_hint=(0.4, None), height=30, bold=True, halign='right'))
        layout.add_widget(Label(text=text2, size_hint=(0.6, None), height=30, halign='right'))
        layout_.add_widget(layout)
        return layout_

    def create_label(self, text):
        layout = StackLayout(orientation='vertical', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text, size_hint=(1.0, None), height=30, bold=True, halign='right'))
        layout_.add_widget(layout)
        return layout_


class APIApp(App):
    pass


if __name__ == '__main__':
    APIApp().run()
