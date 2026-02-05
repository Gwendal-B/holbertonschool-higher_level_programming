import csv
import json

# Import des classes
from centaure import Centaure
from acromentule import Acromentule
from detraqueur import Detraqueur
from dragon import Dragon
from elfedemaison import ElfeDeMaison

def lire_csv(nom_fichier):
    """Lit le fichier CSV et retourne les données"""
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            return list(lecteur)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

def creer_creature(type_creature, donnees):
    """Crée une instance de créature selon son type"""


def sauvegarder_json(creatures, nom_fichier):
    """Sauvegarde les créatures dans un fichier JSON"""
    try:
        # Convertir les objets en dictionnaire avec l'ID comme clé


        # Sauvegarder dans le fichier JSON
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees_json, fichier, indent=2, ensure_ascii=False)

        print(f"Données sauvegardées avec succès dans {nom_fichier}")
        print(f"Nombre de créatures sauvegardées : {len(donnees_json)}")

    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def main():
    """Fonction principale"""
    print("=== Gestionnaire de Créatures Magiques ===")

    # 1. Lire le fichier CSV
    print("Lecture du fichier creatures.csv...")
    donnees_csv = lire_csv('creatures.csv')
    print(donnees_csv)

    if not donnees_csv:
        print("Aucune donnée à traiter.")
        return

    # 2. Créer les objets créatures
    print("Création des objets créatures...")
    creatures = []


    # 3. Sauvegarder en JSON
    print("\nSauvegarde dans data.json...")
    sauvegarder_json(creatures, 'data.json')

    print("\n=== Traitement terminé ===")

if __name__ == "__main__":
    main()
