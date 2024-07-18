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
        
        print("Initializing CustomBoxLayout...")  # Print debug message
        
        # Setting background color and binding size/position updates
        with self.canvas.before:
            Color(*bg_color)  # Set the background color using RGBA values
            self.rect = Rectangle(size=self.size, pos=self.pos)  # Create a rectangle with the specified size and position
        
        # Bind size and position updates to the _update_rect method
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        # Update the position and size of the rectangle to match the instance's position and size
        self.rect.pos = instance.pos
        self.rect.size = instance.size



class OrderView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Initializing Order View...")  # Debugging line
        
        # Create a StackLayout to hold order items
        self.layout = StackLayout(orientation='lr-tb', padding=10, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))  # Bind height to adjust based on content
        self.add_widget(self.layout)  # Add the StackLayout to the ScrollView
        self.load_orders()  # Load orders upon initialization

    def load_orders(self):
        try:
            print("Attempting to fetch orders...")  # Debugging line
            
            # Fetch data from the specified URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)
            data = response.json()  # Parse the JSON response
            orders = data.get('order', [])  # Extract 'order' data from JSON
            
            print(f"Orders data received: {orders}")  # Debugging line

            if orders:
                # Iterate through each order details
                for order_details in orders:
                    # Extract relevant order details
                    order_id = order_details['id']
                    order_name = order_details['name']
                    order_phone = order_details['phone']
                    order_email = order_details['email']
                    order_address = order_details['address']
                    order_date = order_details['order_date']
                    ordered_products = json.loads(order_details['ordered_products'])
                    totale = order_details['total']
                    
                    # Create an OrderItem instance with extracted details
                    item = OrderItem(order_id, order_name, order_phone, order_email, order_address, order_date,
                                     ordered_products, totale)
                    
                    # Add the OrderItem to the StackLayout
                    self.layout.add_widget(item)
            else:
                print("No orders found")  # Debugging line
        except Exception as e:
            print("Error loading orders:", e)  # Debugging line


class OrderItem(StackLayout):
    # Define properties for order details
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
        
        # Set layout properties
        self.orientation = 'lr-tb'
        self.padding = 10
        self.spacing = 20
        self.size_hint_y = None
        self.height = self.minimum_height

        # Initialize order details
        self.numero_de_commande = "#" + str(numero_de_commande)
        self.order_name = str(order_name)
        self.order_phone = str(order_phone)
        self.order_email = str(order_email)
        self.order_address = str(order_address)
        self.order_date = str(order_date)
        
        # Format order date for display
        self.order_date_s = self.order_date.split("T")  # Split the date at 'T'
        date_part = self.order_date_s[0]  # Extract the date part
        time_part = self.order_date_s[1].split(".")[0]  # Extract the time part without milliseconds
        result = date_part + " " + time_part  # Combine date and time with a space
        print(f"Formatted date: {result}")  # Debugging line
        self.order_date = result
        
        self.totale_str = f"{totale} DH"  # Format total amount
        
        # Add order details to the layout
        self.add_widget(self.create_label_pair("Facture de commande", self.numero_de_commande))
        self.add_widget(self.create_label_pair("Nom du client:", self.order_name))
        self.add_widget(self.create_label_pair("Téléphone:", self.order_phone))
        self.add_widget(self.create_label_pair("Email:", self.order_email))
        self.add_widget(self.create_label_pair("Adresse:", self.order_address))
        self.add_widget(self.create_label_pair("Date de la commande:", self.order_date))

        self.add_widget(self.create_label("Produits commandés:"))  # Add section header
        for product in ordered_products:
            product_name = str(product['name'])
            product_price = str(product['price']) + " DH"
            self.add_widget(self.create_label_pair(product_name, product_price))  # Add each product entry

        self.add_widget(self.create_label_pair("Totale payé", self.totale_str))  # Add total amount section

    def create_label_pair(self, text1, text2):
        # Create a horizontal StackLayout with two labels aligned right
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text1, size_hint=(0.4, None), height=30, bold=True, halign='right'))
        layout.add_widget(Label(text=text2, size_hint=(0.6, None), height=30, halign='right'))
        layout_.add_widget(layout)
        return layout_

    def create_label(self, text):
        # Create a vertical StackLayout with a bold label aligned right
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        layout.add_widget(Label(text=text, size_hint=(1.0, None), height=30, bold=True, halign='right'))
        layout_.add_widget(layout)
        return layout_


class ReservationView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Initializing Reservation View...")  # Debugging line
        
        # Create a StackLayout to hold reservation items
        self.layout = StackLayout(orientation='lr-tb', padding=10, spacing=30, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))  # Bind height to adjust based on content
        self.add_widget(self.layout)  # Add the StackLayout to the ScrollView
        self.load_reservations()  # Load reservations upon initialization

    def load_reservations(self):
        try:
            print("Attempting to fetch reservations...")  # Debugging line
            
            # Fetch data from the specified URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)
            data = response.json()  # Parse the JSON response
            reservations = data.get('reservation', [])  # Extract 'reservation' data from JSON
            
            print(f"Reservations data received: {reservations}")  # Debugging line

            if reservations:
                # Iterate through each reservation details
                for reservation_details in reservations:
                    # Extract relevant reservation details
                    reservation_id = reservation_details['id']
                    reservation_name = reservation_details['name']
                    reservation_phone = reservation_details['phone']
                    reservation_email = reservation_details['email']
                    reservation_date = reservation_details['date']
                    reservation_time = reservation_details['time']
                    reservation_guests = reservation_details['guests']
                    
                    # Create a ReservationItem instance with extracted details
                    item = ReservationItem(reservation_id, reservation_name, reservation_phone, reservation_email,
                                           reservation_date, reservation_time, reservation_guests)
                    
                    # Add the ReservationItem to the StackLayout
                    self.layout.add_widget(item)
            else:
                print("No reservations found")  # Debugging line
        except Exception as e:
            print("Error loading reservations:", e)  # Debugging line


class ReservationItem(StackLayout):
    # Define StringProperties for reservation details
    id = StringProperty()
    nom = StringProperty()
    phone = StringProperty()
    email = StringProperty()
    date = StringProperty()
    hour = StringProperty()
    nb_invited = StringProperty()

    def __init__(self, id, nom, phone, email, date, hour, nb_invited, **kwargs):
        super().__init__(**kwargs)
        
        # Set layout properties
        self.orientation = 'lr-tb'  # Set orientation of the StackLayout
        self.padding = 10  # Set padding around the layout
        self.spacing = 20  # Set spacing between widgets
        self.size_hint_y = None  # Ensure the height is determined by content
        self.height = self.minimum_height  # Set initial height based on minimum required

        # Initialize properties with provided values
        self.id = "#" + str(id)  # Format ID with a prefix
        self.nom = str(nom)  # Name of the reservation holder
        self.phone = str(phone)  # Contact phone number
        self.email = str(email)  # Contact email
        self.date = str(date)  # Date of the reservation
        self.hour = str(hour)  # Time of the reservation
        self.nb_invited = str(nb_invited)  # Number of guests

        # Add widgets to display reservation details
        self.add_widget(self.create_label_pair("Réservation", self.id))  # Title and ID pair
        self.add_widget(self.create_label_pair("Nom:", self.nom))  # Name label pair
        self.add_widget(self.create_label_pair("Téléphone:", self.phone))  # Phone label pair
        self.add_widget(self.create_label_pair("Email:", self.email))  # Email label pair
        self.add_widget(self.create_label_pair("Date:", self.date))  # Date label pair
        self.add_widget(self.create_label_pair("Heure:", self.hour))  # Time label pair
        self.add_widget(self.create_label_pair("Nombre de convives:", self.nb_invited))  # Guests label pair

    def create_label_pair(self, text1, text2):
        # Create a horizontal StackLayout for a label pair
        layout = StackLayout(orientation='lr-tb', size_hint=(1, None), height=30)
        # Create a CustomBoxLayout with vertical orientation for styling
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        # Add labels with specified text and formatting
        layout.add_widget(Label(text=text1, size_hint=(0.4, None), height=30, bold=True, halign='right'))
        layout.add_widget(Label(text=text2, size_hint=(0.6, None), height=30, halign='right'))
        layout_.add_widget(layout)  # Add horizontal layout to vertical layout for complete pair
        return layout_

    def create_label(self, text):
        # Create a vertical StackLayout for a single label
        layout = StackLayout(orientation='vertical', size_hint=(1, None), height=30)
        # Create a CustomBoxLayout with vertical orientation for styling
        layout_ = CustomBoxLayout(orientation='vertical', size_hint=(1, None), height=30, bg_color=(0.3, 0.3, 0.3, 1))
        # Add label with specified text and formatting
        layout.add_widget(Label(text=text, size_hint=(1.0, None), height=30, bold=True, halign='right'))
        layout_.add_widget(layout)  # Add vertical layout to vertical layout for styling
        return layout_



class APIApp(App):
    pass

if __name__ == '__main__':
    print("Starting the application...")  # Print a message indicating the application is starting
    APIApp().run()
