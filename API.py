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

            # Afficher la facture
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
else:
    print_red(f"Échec de la requête. Code de statut: {response.status_code}")