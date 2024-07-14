from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import requests
import json


class OrderViewer(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orders = []
        self.url = 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data'
        self.refresh_interval = 60  # Interval de rafraîchissement en secondes

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # ScrollView with adjusted size
        self.scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        self.orders_stack = StackLayout(size_hint=(1, None), spacing=10, padding=10)
        self.scrollview.add_widget(self.orders_stack)

        self.layout.add_widget(self.scrollview)

        # Refresh button with adjusted size
        self.refresh_button = Button(text="Rafraîchir les données", size_hint=(1, None), height=dp(20))
        self.refresh_button.bind(on_press=self.refresh_data)
        self.layout.add_widget(self.refresh_button)

        self.load_data()  # Charger les données au démarrage
        self.schedule_data_refresh()

        return self.layout

    def refresh_data(self, instance):
        self.load_data()

    def load_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lève une exception pour les codes de statut d'erreur
            self.orders = response.json().get('order', [])
            self.update_orders_stack()
        except requests.RequestException as e:
            self.orders_stack.clear_widgets()
            self.orders_stack.add_widget(Label(text=f"Échec de la requête : {e}", size_hint=(1, None), height=40))

    def update_orders_stack(self):
        self.orders_stack.clear_widgets()
        for order_details in self.orders:
            order_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(600, Window.height * 0.6),
                                     padding=15, spacing=10)
            order_layout.bind(minimum_height=order_layout.setter('height'))

            with order_layout.canvas.before:
                Color(0.9, 0.9, 0.9, 1)
                order_rect = Rectangle(size=order_layout.size, pos=order_layout.pos)
                order_layout.bind(size=self._update_rect(order_rect, order_layout),
                                  pos=self._update_rect(order_rect, order_layout))

            order_id = order_details['id']
            order_name = order_details['name']
            order_phone = order_details['phone']
            order_email = order_details['email']
            order_address = order_details['address']
            order_date = order_details['order_date']
            total_amount = order_details['total']
            ordered_products = json.loads(order_details['ordered_products'])

            order_layout.add_widget(self.create_order_label(f"[b]Facture de commande #{order_id}[/b]", bold=True))
            order_layout.add_widget(self.create_order_label(f"Nom du client:\n{order_name}"))
            order_layout.add_widget(self.create_order_label(f"Téléphone:\n{order_phone}"))
            order_layout.add_widget(self.create_order_label(f"Email:\n{order_email}"))
            order_layout.add_widget(self.create_order_label(f"Adresse:\n{order_address}"))
            order_layout.add_widget(self.create_order_label(f"Date de la commande:\n{order_date}"))

            order_layout.add_widget(self.create_order_label("\nProduits commandés:", bold=True))
            products_grid = GridLayout(cols=2, size_hint=(1, None), spacing=5)
            products_grid.bind(minimum_height=products_grid.setter('height'))
            products_grid.add_widget(self.create_order_label("Nom", bold=True))
            products_grid.add_widget(self.create_order_label("Prix", bold=True, align_right=True))

            for product in ordered_products:
                product_name = product['name']
                product_price = product['price']
                products_grid.add_widget(self.create_order_label(product_name))
                products_grid.add_widget(self.create_order_label(f"${product_price:.2f}", align_right=True))

            order_layout.add_widget(products_grid)
            order_layout.add_widget(self.create_order_label(f"\nTotal à payer: ${total_amount:.2f}", bold=True))

            self.orders_stack.add_widget(order_layout)

        # Update the height of the orders_stack and scrollview based on content
        self.orders_stack.height = sum(child.height + 10 for child in self.orders_stack.children)
        self.scrollview.height = min(self.orders_stack.height, Window.height - 50)

    def create_order_label(self, text, bold=False, align_right=False):
        halign = 'right' if align_right else 'left'
        return Label(
            text=text,
            size_hint=(1, None),
            height=40,
            markup=True,
            color=(0, 0, 0, 1),
            bold=bold,
            halign=halign,
            valign='middle',
            text_size=(None, None)  # Important for multiline
        )

    def _update_rect(self, rect, layout):
        def update(instance, value):
            rect.size = layout.size
            rect.pos = layout.pos

        return update

    def schedule_data_refresh(self):
        Clock.schedule_interval(lambda dt: self.load_data(), self.refresh_interval)


if __name__ == '__main__':
    OrderViewer().run()
