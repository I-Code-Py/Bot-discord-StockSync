# Bot Discord Earn (Avec Hebergement, Gestion du stock, Option de payement, 
>Discord earn est un projet crée pour une commauté privée voulant un bot marchant sur Discord. Le bot sert a prendre des réservation sur une actions proposé en échange du commission pour le travail effectué. Le bot peut êre modifier pour des devellopeur voulant vendre un produit avec un système de payement intégré lier à un compte Stirpe ou voulant un bot de gestion de places pour un évenement avec un système de réservation.

> [!NOTE]
> Les fonctionnalitré et l'utilisation du bot ont été concu pour rendre le processus totalement gratuit avec l'utilisation gratuite de Replit pour l'hebergement du bot et du système UI ansi que Firebase de Google pour l'hebergement de la base de doonées. Il est possible d'utiliser uniquement Replit mais cela rendra le bot plus lent. Pour de  meilleur éfficacitée, nous vous recommandons de passer par un hebergement gratuit d'un serveur comme le propose Google pour avoir des performances bien plus élevé https://cloud.google.com/free?hl=fr

avec une interface Web UI ainsi qu'une connexion a une base de doonées qui indique le nombre de place disponible pour un événement. Le bot a été dévellopé en python pour une plus grande facilité d'usage et de modification au long terme. L'idée de crée un bot avec node.js a été abandoonées après que l'équipe du projet c'est rendu compte de la difficulté du language comparé au python.

Le texte en Rouge signifie que la fonction est réservé au administrateur
Le texte en Bleu signifie que la fonction est disponible pour les utilisateurs

Le bot a comme fonction principale pour les administrateurs du réseau :
- Création d'évenement/ Poduits (synchronyser avec une base de doonées hébergé par Google Firebase)
- Gestion du stock synchronyser avec la base de doonées et avec une interface UI; possibilité de modification du stock et des réservation sur l'interface UI hébergé en local chez un des administrateurs pour éviter des abus de tiers qui pourrait prendre le controle du bot.
- Pssibilité de gérer la gestion des stock en ligne de commande directement sur discord.
