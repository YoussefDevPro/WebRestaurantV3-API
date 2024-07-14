$(document).ready(function() {
    // Fonction pour charger les données des commandes et des réservations
    function loadData() {
        $.ajax({
            url: 'http://127.0.0.1:8000/API/IRVRVHNOIUNOUZHNOZIJNC/Get-All-Json-Data',
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                // Traiter les données reçues et les afficher
                displayOrders(data.order);
                displayReservations(data.reservation);
            },
            error: function(error) {
                console.error('Échec de la requête:', error);
                displayError('Échec de la requête');
            }
        });
    }

    // Fonction pour afficher les données des commandes
    function displayOrders(orders) {
        var ordersContainer = document.getElementById('orders-container');
        ordersContainer.innerHTML = ''; // Effacer le contenu précédent

        if (!orders || orders.length === 0) {
            displayError('Aucune commande trouvée.');
            return;
        }

        // Parcourir les commandes et les ajouter au conteneur
        orders.forEach(function(order) {
            var orderElement = document.createElement('div');
            orderElement.classList.add('order');

            // Construire le HTML pour chaque commande
            var productsHTML = JSON.parse(order.ordered_products).map(function(product) {
                return `<li>${product.name} - ${product.price}</li>`;
            }).join('');

            orderElement.innerHTML = `
                <h2>Facture de commande #${order.id}</h2>
                <p>Nom du client: ${order.name}</p>
                <p>Téléphone: ${order.phone}</p>
                <p>Email: ${order.email}</p>
                <p>Adresse: ${order.address}</p>
                <p>Date de la commande: ${new Date(order.order_date).toLocaleString()}</p>
                <h3>Produits commandés:</h3>
                <ul>${productsHTML}</ul>
                <p>Total à payer: $${order.total.toFixed(2)}</p>
            `;

            ordersContainer.appendChild(orderElement);
        });
    }

    // Fonction pour afficher les données des réservations
    function displayReservations(reservations) {
        var reservationsContainer = document.getElementById('reservations-container');
        reservationsContainer.innerHTML = ''; // Effacer le contenu précédent

        if (!reservations || reservations.length === 0) {
            displayError('Aucune réservation trouvée.');
            return;
        }

        // Parcourir les réservations et les ajouter au conteneur
        reservations.forEach(function(reservation) {
            var reservationElement = document.createElement('div');
            reservationElement.classList.add('reservation');

            // Construire le HTML pour chaque réservation
            reservationElement.innerHTML = `
                <h2>Réservation #${reservation.id}</h2>
                <p>Nom: ${reservation.name}</p>
                <p>Email: ${reservation.email}</p>
                <p>Téléphone: ${reservation.phone}</p>
                <p>Date: ${reservation.date} ${reservation.time}</p>
                <p>Nombre d'invités: ${reservation.guests}</p>
            `;

            reservationsContainer.appendChild(reservationElement);
        });
    }

    // Fonction pour afficher les erreurs
    function displayError(message) {
        var errorElement = document.createElement('div');
        errorElement.classList.add('error');
        errorElement.textContent = message;

        var ordersContainer = document.getElementById('orders-container');
        ordersContainer.innerHTML = ''; // Effacer le contenu précédent
        ordersContainer.appendChild(errorElement);

        var reservationsContainer = document.getElementById('reservations-container');
        reservationsContainer.innerHTML = ''; // Effacer le contenu précédent
        reservationsContainer.appendChild(errorElement.cloneNode(true));
    }

    // Charger les données au chargement de la page et rafraîchir toutes les minutes
    loadData();
    setInterval(loadData, 60000); // Rafraîchir toutes les 60 secondes (60000 millisecondes)
});
