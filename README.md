# StockSync 📦 (Avec Hébergement, Gestion du Stock, Option de Paiement)  

**StockSync** est un projet conçu pour une communauté privée souhaitant un bot fonctionnant sur Discord. Ce bot permet de prendre des réservations sur une action proposée, en échange d'une commission pour le travail effectué. StockSync peut également être modifié pour les développeurs souhaitant :  
- Vendre un produit avec un système de paiement intégré, lié à un compte Stripe ou PayPal.  
- Gérer des places pour un événement avec un système de réservation synchronisé.  
- Créer un programme d’affiliation gagnant-gagnant, où l’administrateur perçoit une commission sur les ventes effectuées par les utilisateurs, tout en récompensant ces derniers pour leur participation.  

> **Note :**  
> Les fonctionnalités et l'utilisation du bot ont été conçues pour rendre le processus totalement gratuit grâce à l'utilisation gratuite de Replit pour l'hébergement du bot et de l'interface utilisateur (UI), ainsi que Firebase de Google pour l'hébergement de la base de données. Il est possible d'utiliser uniquement Replit, mais cela pourrait ralentir le bot. Pour de meilleures performances, nous vous recommandons de passer par un hébergement gratuit d'un serveur comme [Google Cloud](https://cloud.google.com/free?hl=fr).  

---

## Fonctionnalités  

🔴 **Fonctionnalités réservées aux administrateurs :**  
- Création d’événements ou de produits (synchronisé avec une base de données hébergée par Google Firebase).  
- Gestion du stock synchronisé avec la base de données, accessible via une interface UI.  
  - L’interface est hébergée localement par un administrateur pour éviter les abus de tiers.  
- Gestion des stocks via commandes directement sur Discord.  
- Consultation des réservations des utilisateurs avec la commande `!stats`.  

🔵 **Fonctionnalités accessibles aux utilisateurs :**  
- Création d'un salon privé pour interagir avec le bot ou un membre de l'administration via la commande `!start`.  
- Fermeture du salon privé (maximum : 1 salon par utilisateur) avec `!close`.  
- Réservation de produits ou d'options (`!reserver <nom produit> <quantité>`).  
- Annulation des réservations (`!annuler <nom produit> <quantité>`).  
- Paiement sécurisé via l'API de Stripe ou PayPal.  
- Utilisation des boutons interactifs pour gérer les réservations, annulations, fermetures de salon privé et choix du mode de paiement.  

---

## Fonctionnement du bot  

### Programme d'affiliation  
**StockSync** inclut une option de programme d’affiliation, permettant :  
- Aux administrateurs de générer des revenus en prenant une commission sur les ventes effectuées.  
- Aux utilisateurs de recevoir des récompenses pour leur participation ou leur implication dans les ventes.  

Les gains sont calculés automatiquement et stockés dans la base de données, permettant une transparence totale.  

---

## Limitations de Replit  

Bien que Replit soit une solution gratuite et pratique pour héberger StockSync, il n'est pas recommandé pour une utilisation à long terme en raison des limitations suivantes :  
- Performances limitées : Risque de ralentissements pour un bot avec beaucoup d'utilisateurs.  
- Temps d'inactivité : Les projets gratuits sur Replit sont mis en veille après une période d'inactivité.  
- Sécurité moindre : Héberger des clés API sensibles (Stripe, Firebase) sur Replit peut être risqué pour des projets en production.
- Blocage après un certain temps d'activitées (25h par mois il me semble)

**Recommandation :** Migrez vers une plateforme plus performante comme :  
- Google Cloud  
- Amazon AWS  
- Un serveur VPS (comme OVH ou DigitalOcean).  

---

## Avancée des tâches  

- [x] Possibilité pour les administrateurs d'utiliser la commande `!stats`.  
- [x] Possibilité pour les utilisateurs d'utiliser les commandes `!start`, `!close`, `!reserver`, `!annuler`.  
- [ ] Ajout des commandes en `/`.  
- [x] Système de gestion de la base de données avec Firebase.  
- [ ] Intégration de l'interface Web UI.  
- [ ] Intégration du processeur de paiement Stripe.  
- [ ] Intégration du processeur de paiement PayPal 🎉.  

---

## Avertissement  

L'utilisation de ce bot est sous votre responsabilité. Assurez-vous de protéger les données sensibles (comme les clés API). Si vous déployez StockSync pour une communauté, respectez les lois locales concernant la confidentialité des données et les transactions financières.  

---

Pour toute assistance, ouvrez une issue sur GitHub ou contactez l'équipe de développement.  
