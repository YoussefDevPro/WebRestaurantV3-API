from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
import requests
import json

url = 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data'

class MainWidget(TabbedPanel):
    pass

class OrderView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        response = requests.get(url)
        if response.status_code == 200:
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
                    totale = order_details['total']
                    ordered_products = json.loads(order_details['ordered_products'])
                    item = OrderItem(order_id, order_name, order_phone, order_email, order_address, order_date, ordered_products, totale)
                    self.add_widget(item)

class OrderedProductItem(BoxLayout):
    nom = StringProperty()
    prix = StringProperty()

    def __init__(self, nom, prix, **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.prix = str(prix) + " DH"

class OrderItem(BoxLayout):
    numero_de_commande = StringProperty()
    order_name = StringProperty()
    order_phone = StringProperty()
    order_email = StringProperty()
    order_address = StringProperty()
    order_date = StringProperty()
    totale_str = StringProperty()

    def __init__(self, numero_de_commande, order_name, order_phone, order_email, order_address, order_date, ordered_products, totale, **kwargs):
        super().__init__(**kwargs)
        self.numero_de_commande = "#" + str(numero_de_commande)
        self.order_name = order_name
        self.order_phone = order_phone
        self.order_email = order_email
        self.order_address = order_address
        self.order_date = order_date

        total = sum(product['price'] for product in ordered_products)
        self.totale_str = f"{total} DH"

        for product in ordered_products:
            product_name = product['name']
            product_price = product['price']
            product_widget = OrderedProductItem(product_name, product_price)
            self.add_widget(product_widget)

        product_widget = OrderedProductItem("Totale payé", totale)
        self.add_widget(product_widget)


class APIApp(App):
    pass


if __name__ == '__main__':
    APIApp().run()

