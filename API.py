import requests
import json

# Fonction pour afficher du texte en rouge dans la console
def print_red(text):
    print("\033[1;31m" + text + "\033[0m")

# Fonction pour afficher du texte en vert dans la console
def print_green(text):
    print("\033[1;32m" + text + "\033[0m")

# Fonction pour afficher du texte en orange dans la console
def print_orange(text):
    print("\033[1;33m" + text + "\033[0m")

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
        for order_details in orders:
            order_id = order_details['id']
            order_name = order_details['name']
            order_phone = order_details['phone']
            order_email = order_details['email']
            order_address = order_details['address']
            order_date = order_details['order_date']
            total_amount = order_details['total']
            ordered_products = json.loads(order_details['ordered_products'])

            # Afficher la facture
            print_red(f"Facture de commande #{order_id}")
            print(f"Nom du client: {order_name}")
            print(f"Téléphone: {order_phone}")
            print(f"Email: {order_email}")
            print(f"Adresse: {order_address}")
            print(f"Date de la commande: {order_date}")
            print("\nProduits commandés:")
            print("{:<20} {:<10}".format("\033[1;31mNom\033[0m", "\033[1;31mPrix\033[0m"))  # Titres en rouge
            for product in ordered_products:
                product_name = product['name']
                product_price = product['price']
                # Affichage du produit avec prix aligné
                print("{:<20} {:<10}".format(product_name, f"${product_price}"))

            # Afficher le total à payer en orange
            print_orange("\nTotal à payer: ${:.2f}".format(total_amount))
            print("\n" + "=" * 50)  # Séparateur visuel entre les factures
    else:
        print("Aucune commande trouvée.")
else:
    print(f"Échec de la requête. Code de statut: {response.status_code}")
