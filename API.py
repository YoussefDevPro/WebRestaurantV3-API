from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import requests
import json
import time


class OrderViewer(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_loaded = False
        self.orders = []
        self.url = 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data'
        self.refresh_interval = 60  # Interval de rafraîchissement en secondes (60 secondes = 1 minute)

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.scrollview = ScrollView()
        self.orders_label = Label(text="Chargement des données...", size_hint=(1, None),
                                  height=1000)  # Hauteur initiale pour activer le défilement
        self.scrollview.add_widget(self.orders_label)
        self.layout.add_widget(self.scrollview)
        self.refresh_button = Button(text="Rafraîchir les données", size_hint=(1, 0.1))
        self.refresh_button.bind(on_press=self.refresh_data)
        self.layout.add_widget(self.refresh_button)
        self.schedule_data_refresh()
        return self.layout

    def refresh_data(self, instance):
        self.load_data()

    def load_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.orders = response.json().get('order', [])
            self.update_orders_label()
        else:
            self.orders_label.text = f"Échec de la requête. Code de statut: {response.status_code}"
        self.data_loaded = True

    def update_orders_label(self):
        orders_text = ""
        for order_details in self.orders:
            order_id = order_details['id']
            order_name = order_details['name']
            order_phone = order_details['phone']
            order_email = order_details['email']
            order_address = order_details['address']
            order_date = order_details['order_date']
            total_amount = order_details['total']
            ordered_products = json.loads(order_details['ordered_products'])

            orders_text += f"\n{'=' * 50}"
            orders_text += f"\nFacture de commande #{order_id}"
            orders_text += f"\n{'Nom du client:':<20} {order_name}"
            orders_text += f"\n{'Téléphone:':<20} {order_phone}"
            orders_text += f"\n{'Email:':<20} {order_email}"
            orders_text += f"\n{'Adresse:':<20} {order_address}"
            orders_text += f"\n{'Date de la commande:':<20} {order_date}"
            orders_text += "\n\nProduits commandés:"
            orders_text += "\n{:<30} {:<10}".format("Nom", "Prix")
            orders_text += "\n" + "-" * 40

            for product in ordered_products:
                product_name = product['name']
                product_price = product['price']
                orders_text += f"\n{product_name:<30} ${product_price:.2f}"

            orders_text += f"\n\nTotal à payer: ${total_amount:.2f}"

        self.orders_label.text = orders_text
        # Mettre à jour la hauteur du Label en fonction du contenu
        self.orders_label.height = self.orders_label.texture_size[
                                       1] + 20  # Ajoutez une marge supplémentaire pour le padding

    def schedule_data_refresh(self):
        Clock.schedule_interval(lambda dt: self.load_data(), self.refresh_interval)


if __name__ == '__main__':
    OrderViewer().run()
