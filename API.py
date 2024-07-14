import requests
import json
import time

# Fonction pour afficher du texte en rouge dans la console
def print_red(text):
    print("\033[1;31m" + text + "\033[0m")

# Fonction pour afficher du texte en vert dans la console
def print_green(text):
    print("\033[1;32m" + text + "\033[0m")

# Fonction pour afficher du texte en orange dans la console
def print_orange(text):
    print("\033[1;33m" + text + "\033[0m")

# Fonction pour afficher du texte en bleu dans la console
def print_blue(text):
    print("\033[1;34m" + text + "\033[0m")

# URL de l'API
url = 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data'

# Effectuer la requête GET pour récupérer les données JSON
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Récupérer les données des commandes
    orders = data.get('order', [])

    # Vérifier s'il y a des commandes à traiter
    if orders:
        print()
        print_blue("Commandes :")
        print("\n" + "=" * 50)
        for order_details in orders:
            time.sleep(0.2)
            order_id = order_details['id']
            order_name = order_details['name']
            order_phone = order_details['phone']
            order_email = order_details['email']
            order_address = order_details['address']
            order_date = order_details['order_date']
            total_amount = order_details['total']
            ordered_products = json.loads(order_details['ordered_products'])

            # Afficher la facture de la commande
            print("\n" + "=" * 50)  # Séparateur visuel entre les factures
            print_red(f"Facture de commande #{order_id}")
            print(f"{'Nom du client:':<20} {order_name}")
            print(f"{'Téléphone:':<20} {order_phone}")
            print(f"{'Email:':<20} {order_email}")
            print(f"{'Adresse:':<20} {order_address}")
            print(f"{'Date de la commande:':<20} {order_date}")
            print("\nProduits commandés:")
            print("{:<30} {:<10}".format("\033[1;31mNom\033[0m", "\033[1;31mPrix\033[0m"))  # Titres en rouge
            print("-" * 40)  # Séparateur

            for product in ordered_products:
                time.sleep(0.1)
                product_name = product['name']
                product_price = product['price']
                # Affichage du produit avec prix aligné
                print("{:<30} {:<10}".format(product_name, f"${product_price:.2f}"))

            # Afficher le total à payer en orange
            print_orange("\nTotal à payer: ${:.2f}".format(total_amount))
            print("\n" + "=" * 50)  # Séparateur visuel entre les factures
    else:
        print_blue("Aucune commande trouvée.")

    # Récupérer les données des réservations
    reservations = data.get('reservation', [])

    # Vérifier s'il y a des réservations à traiter
    if reservations:
        print()
        print_green("Réservations :")
        print("\n" + "=" * 50)
        for reservation_details in reservations:
            time.sleep(0.2)
            reservation_id = reservation_details['id']
            reservation_name = reservation_details['name']
            reservation_phone = reservation_details['phone']
            reservation_email = reservation_details['email']
            reservation_date = reservation_details['date']
            reservation_time = reservation_details['time']
            reservation_guests = reservation_details['guests']

            # Afficher les détails de la réservation
            print("\n" + "=" * 50)  # Séparateur visuel entre les réservations
            print_green(f"Réservation #{reservation_id}")
            print(f"{'Nom:':<20} {reservation_name}")
            print(f"{'Téléphone:':<20} {reservation_phone}")
            print(f"{'Email:':<20} {reservation_email}")
            print(f"{'Date:':<20} {reservation_date}")
            print(f"{'Heure:':<20} {reservation_time}")
            print(f"{'Nombre de convives:':<20} {reservation_guests}")
            print("\n" + "=" * 50)  # Séparateur visuel entre les réservations
    else:
        print_green("Aucune réservation trouvée.")
else:
    print_red(f"Échec de la requête. Code de statut: {response.status_code}")
