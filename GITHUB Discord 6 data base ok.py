from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, firestore
import discord
from discord.ext import commands

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Vérifier si la variable d'environnement est correctement chargée
firebase_key_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
print(f"Chemin vers la clé Firebase : {firebase_key_path}")  # Affiche le chemin pour vérifier

if not firebase_key_path:
    raise ValueError("Le chemin de la clé Firebase n'est pas défini dans le fichier .env.")

# Charger la clé de service Firebase
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)

# Connecter Firestore
db = firestore.client()

# Configuration du bot Discord avec les commandes
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lors de la connexion du bot
@bot.event
async def on_ready():
    print(f'Nous avons connecté {bot.user}')

# Commande !reserver : Réserver une ou plusieurs places (1 place par défaut si non spécifié)
@bot.command()
async def reserver(ctx, nombre: int = 1):
    """ Réserver une ou plusieurs places (1 place par défaut si non spécifié) """
    places_ref = db.collection("places").document("avisGoogle")
    doc = places_ref.get()

    if doc.exists:
        places_data = doc.to_dict()
        places_restantes = places_data.get("placesRestantes", 0)

        if nombre <= places_restantes and nombre > 0:
            # Réduire le nombre de places restantes en fonction de la réservation
            places_ref.update({"placesRestantes": places_restantes - nombre})
            # Ajouter la réservation à l'utilisateur
            user_ref = db.collection("reservations").document(str(ctx.author.id))
            user_data = user_ref.get()

            if user_data.exists:
                user_reservations = user_data.to_dict().get("reservations", 0)
                user_ref.update({"reservations": user_reservations + nombre})
            else:
                user_ref.set({"reservations": nombre})

            await ctx.send(f"Tu as réservé {nombre} place{'s' if nombre > 1 else ''} !")
        else:
            await ctx.send(f"Il n'y a pas assez de places disponibles. Il reste {places_restantes} place{'s' if places_restantes > 1 else ''}.")
    else:
        await ctx.send("Aucune donnée sur les places n'a été trouvée.")

# Commande !annuler : Annuler une réservation (réservé aux administrateurs)
@bot.command()
async def annuler(ctx):
    """ Commande !annuler : Annuler une réservation (réservé aux administrateurs) """
    # Vérifie si l'utilisateur est administrateur
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("Tu n'as pas les permissions nécessaires pour annuler une réservation.")
        return

    # Annuler une réservation d'un utilisateur
    user_ref = db.collection("reservations").document(str(ctx.author.id))
    user_data = user_ref.get()

    if user_data.exists:
        user_reservations = user_data.to_dict().get("reservations", 0)

        if user_reservations > 0:
            # Rendre la place disponible à nouveau
            places_ref = db.collection("places").document("avisGoogle")
            places_data = places_ref.get().to_dict()
            places_restantes = places_data.get("placesRestantes", 0)

            places_ref.update({"placesRestantes": places_restantes + 1})
            user_ref.update({"reservations": 0})
            await ctx.send("Ta réservation a été annulée avec succès.")
        else:
            await ctx.send("Tu n'as aucune réservation à annuler.")
    else:
        await ctx.send("Aucune réservation trouvée pour cet utilisateur.")

# Commande !stats : Afficher les réservations des utilisateurs (réservé aux administrateurs)
@bot.command()
async def stats(ctx):
    """ Commande !stats : Afficher les réservations des utilisateurs (réservé aux administrateurs) """
    # Vérifie si l'utilisateur est administrateur
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("Tu n'as pas les permissions nécessaires pour voir les statistiques.")
        return

    # Récupérer et afficher toutes les réservations des utilisateurs
    reservations_ref = db.collection("reservations")
    docs = reservations_ref.stream()

    message = "Réservations des utilisateurs :\n"
    for doc in docs:
        data = doc.to_dict()
        user_id = doc.id
        reservations = data.get("reservations", 0)
        user = await bot.fetch_user(user_id)

        message += f"{user.name} ({user_id}) - {reservations} place{'s' if reservations > 1 else ''}\n"

    if message == "Réservations des utilisateurs :\n":
        message = "Aucune réservation trouvée."

    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # Envoie un message d'erreur si la commande n'est pas trouvée
        await ctx.send(f"Désolé, mais je ne comprends pas la commande **{ctx.message.content}**")

# Démarrer le bot avec le token Discord
bot.run(os.getenv("DISCORD_TOKEN"))