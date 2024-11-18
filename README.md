# Bot Discord Earn (Avec Hebergement, Gestion du stock, Option de payement, 
>Discord earn est un projet crée pour une commauté privée voulant un bot marchant sur Discord. Le bot sert a prendre des réservation sur une actions proposé en échange du commission pour le travail effectué. Le bot peut êre modifier pour des devellopeur voulant vendre un produit avec un système de payement intégré lier à un compte Stirpe ou voulant un bot de gestion de places pour un évenement avec un système de réservation.

> [!NOTE]
> Les fonctionnalitré et l'utilisation du bot ont été concu pour rendre le processus totalement gratuit avec l'utilisation gratuite de Replit pour l'hebergement du bot et du système UI ansi que Firebase de Google pour l'hebergement de la base de doonées. Il est possible d'utiliser uniquement Replit mais cela rendra le bot plus lent. Pour de  meilleur éfficacitée, nous vous recommandons de passer par un hebergement gratuit d'un serveur comme [le propose Google](https://cloud.google.com/free?hl=fr) pour avoir des performances bien plus élevé 

avec une interface Web UI ainsi qu'une connexion a une base de doonées qui indique le nombre de place disponible pour un événement. Le bot a été dévellopé en python pour une plus grande facilité d'usage et de modification au long terme. L'idée de crée un bot avec node.js a été abandoonées après que l'équipe du projet c'est rendu compte de la difficulté du language comparé au python.

# Fonctionnalitées
🔴 **La partie ROUGE** signifie que la fonction est réservée aux administrateurs.
- Création d'évenement/ Poduits (synchronyser avec une base de doonées hébergé par Google Firebase)
- Gestion du stock synchronyser avec la base de doonées et avec une interface UI; possibilité de modification du stock et des réservation sur l'interface UI hébergé en local chez un des administrateurs pour éviter des abus de tiers qui pourrait prendre le controle du bot.
- Possibilité de gérer la gestion des stock en lignes de commandes directement sur discord.
- Voir les réservations de chaques personnes graces à la commandes '''!stats'''


🔵 **La partie BLEU** signifie que la fonction est disponible pour les utilisateurs.
- Créaton de salon privé pour intéragire avec le bot ou un memebre de l'administration '''!start'''
- Possibilité de fermer son salons ouverts (max : 1 salon par utilisateur) '''!close'''
- Possibilité de réserver des Options en choissisant le nombre (exemple : Ticket salle de cinéma) '''!reserver <nom produit> <quantité>'''
- Possibilité d'annuler les réservations en choisisant le nombre '''!annuler <nom produit> <quantité>'''
- Possibilité de payer avec une Carte bancaire de façons sécurisé grace à l'API du processeur de payement Stripe (Ou paypal)
- possibilité de réservation, d'annulation, fermer son salon privé, choisir son mode de payement avec les boutons du BOT (à l'ouverture du salon privé)


# Avancer des tâches 
- [x] Possibilité pour les administrateur dutiliser les commandes stats
- [x] Système de gestion de la base de doonées avec les commandes directement sur discord
- [ ] Intégration de l'interface web UI
- [ ] Intégration du procésseur de payement Stripe
- [ ] Integration du processeur de payement Paypal  :tada:

# Utilisation du BOT
