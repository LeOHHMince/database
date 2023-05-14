import csv
import matplotlib.pyplot as plt
import folium 

# Initialiser les variables pour chaque colonne
nb_vote_blanc = 0
nb_vote_nul = 0
nb_exprime = 0
macron_emmanuel = 0
le_pen_marine = 0


# Ouvrir le fichier CSV en mode lecture
with open("database.csv", "r") as fichier_csv:
    # Créer un lecteur CSV
    lecteur_csv = csv.DictReader(fichier_csv, delimiter=";")  # Spécifiez le délimiteur comme point-virgule

    # Itérer sur chaque ligne
    for ligne in lecteur_csv:
        # Ajouter la valeur de chaque colonne à sa variable respective
        nb_vote_blanc += float(ligne["nb_vote_blanc"])
        nb_vote_nul += float(ligne["nb_vote_nul"])
        nb_exprime += float(ligne["nb_exprime"])
        macron_emmanuel += float(ligne["macron_emmanuel"])
        le_pen_marine += float(ligne["le_pen_marine"])

score = ""
candidat = ""


# Créer un dictionnaire avec les données
donnees = {
    "nb_vote_blanc": nb_vote_blanc,
    "nb_vote_nul": nb_vote_nul,
    "nb_exprime": nb_exprime,
    "macron_emmanuel": macron_emmanuel,
    "le_pen_marine": le_pen_marine,
    "score" : "",
    "candidat" : ""

}

# Afficher le résultat pour chaque colonne
print("Nombre de votes blancs :", nb_vote_blanc)
print("Nombre de votes nuls :", nb_vote_nul)
print("Nombre de votes exprimés :", nb_exprime)
print("Nombre de votes pour Emmanuel Macron :", macron_emmanuel)
print("Nombre de votes pour Marine Le Pen :", le_pen_marine)



netvotemanu = round((macron_emmanuel / nb_exprime) * 100, 2)
netvotemarine  = round((le_pen_marine / nb_exprime) * 100, 2)



#Partie graphique

# Données
labels = ['Emmanuel Macron', 'Autres']
pourcentages = [netvotemanu, 100-netvotemanu]
# Créer un graphique en camembert avec les pourcentages
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
# Ajouter un titre
ax.set_title("Répartition des votes en île de France en %")
# Exporter le graphique sous forme d'image
fig.savefig("Figure1.png")
# Afficher un message pour confirmer que l'image a été enregistrée
print("Graphique enregistré sous le nom de Figure1.png")



labels = ['Marine Lepen', 'Autres']
pourcentages = [netvotemarine, 100-netvotemarine]
fig, ax = plt.subplots()
ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')
ax.set_title("Répartition des votes en île de France en %")
fig.savefig("Figure2.png")
print("Graphique enregistré sous le nom de Figure2.png")



#Partie interraction avec l'utilisateur

candidat = int(input( "\n 1: Emmanuel Macron \n 5 : Marine Le Pen \n Quel candidat voulez-vous choisir :" ))

lut = {1: ("macron_emmanuel", "Emmanuel Macron"),
       2: ("le_pen_marine", "Marine Le Pen"),}

candidat_key = lut[candidat][0]
candidat_name = lut[candidat][1]

pourcentage_score = round((donnees[candidat_key] / nb_exprime) * 100, 2)

fichier_csv = "log.csv"
with open(fichier_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["candidat", "score_en_pourcentages", "nb_voies"])
    writer.writerow([candidat_name, pourcentage_score, donnees[candidat_key]])

print(f"{candidat_name} a obtenu {pourcentage_score}% des votes du premier tour")





#test folium


map = folium.Map(location=[48.856614,48.856614], zoom_start=12)

for n in lecteur_csv:
    if n[macron_emmanuel]











