#!/usr/bin/python3
# Exercice Python - Inheritance & Abstract Classes
# Univers : Créatures Magiques

"""
OBJECTIF:
Créer un système de créatures magiques en utilisant :
- l'héritage
- les classes abstraites
- les méthodes abstraites
- l'encapsulation

CONSIGNES GÉNÉRALES:
- Respecte la POO (attributs privés, getters/setters)
- Utilise ABC et abstractmethod
- Ne modifie pas le code de test
- Complète uniquement les parties indiquées par TODO

"""

from abc import ABC, abstractmethod
import random


class CreatureMagique(ABC):
    """
    Classe abstraite représentant une créature magique
    """

    def __init__(self, nom, dangerosite):
        """
        Attributs:
        - nom (str)
        - dangerosite (int entre 1 et 10)
        Tous les attributs doivent être privés
        """
        self.__nom = nom
        if 1 <= dangerosite <= 10:
            self.__dangerosite = dangerosite
        else:
            raise ValueError("La dangerosité doit être entre 1 et 10")

    @property
    def nom(self):
        return self.__nom

    @property
    def dangerosite(self):
        return self.__dangerosite

    @abstractmethod
    def attaquer(self):
        """
        Méthode abstraite
        Chaque créature attaque différemment
        """
        pass

    @abstractmethod
    def decrire(self):
        """
        Méthode abstraite
        Retourne une description de la créature
        """
        pass


class Dragon(CreatureMagique):
    """
    Classe Dragon héritant de CreatureMagique
    """

    def __init__(self, nom, dangerosite, couleur_flamme):
        """
        Attribut supplémentaire:
        - couleur_flamme (str)
        """
        super().__init__(nom, dangerosite)
        self.__couleur_flamme = couleur_flamme

    def attaquer(self):
        """
        Affiche une attaque basée sur le feu
        """
        degats = random.randint(1, self.dangerosite * 10)
        if  10 >= degats:
            print(f"{self.nom}, s'etouffe avec son souffle {self.__couleur_flamme} et s'inflige {degats} points de dégats contre lui-même. Cause : echec critique")
        else :
            print(f"{self.nom}, crache un souffle de feu {self.__couleur_flamme} et inflige {degats} points de dégats")

    def decrire(self):
        """
        Retourne une description complète du dragon
        """
        return f"Dragon {self.nom}: dangerosité : {self.dangerosite}, souffle de feu {self.__couleur_flamme}"


class Elfe(CreatureMagique):
    """
    Classe Elfe héritant de CreatureMagique
    """

    def __init__(self, nom, dangerosite, clan):
        """
        Attribut supplémentaire:
        - clan (str)
        """
        super().__init__(nom, dangerosite)
        self.__clan = clan

    def attaquer(self):
        """
        Affiche une attaque basée sur l'arc ou la magie
        """
        degats = random.randint(1, self.dangerosite * 3)
        style = random.choice(["tir à l'arc", "sort de magie"])
        if 4 >= degats and style == "tir à l'arc":
            print(f"{self.nom} envoie une fleche avec un {style} et par malchance la fleche recoche et lui revient dessus, il prend {degats} points de dégats. Cause : echec critique")
        elif 4 >= degats and style == "sort de magie":
            print(f"{self.nom} envoie {style} mais par malchance le sort lui explose au visage, il prend {degats} points de dégats. Cause : echec critique")
        else:
            print(f"{self.nom} attaque avec {style} et inflige {degats} points de dégats")

    def decrire(self):
        """
        Retourne une description complète de l'elfe
        """
        return f"Elfe {self.nom} du clan {self.__clan}: dangerosité {self.dangerosite}"


class Balrog(CreatureMagique):
    """
    Classe Balrog - démon de feu et d'ombre
    """

    def __init__(self, nom, dangerosite, arme):
        """
        Attribut supplémentaire:
        - arme (str): fouet enflammé, épée de feu, etc.
        """
        super().__init__(nom, dangerosite)
        self.__arme = arme

    def attaquer(self):
        """
        Attaque avec feu et ténèbres
        """
        degats = random.randint(1, self.dangerosite * 12)
        attaque_type = random.choice(["flammes", self.__arme, "ténèbres"])

        if 10 >= degats:
            print(f"{self.nom} trébuche dans ses propres flammes et subit {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} frappe avec {attaque_type} dans un rugissement terrible et inflige {degats} points de dégâts")

    def decrire(self):
        """
        Retourne une description complète du Balrog
        """
        return f"Balrog {self.nom}: dangerosité {self.dangerosite}, arme principale {self.__arme}"


class Nazgul(CreatureMagique):
    """
    Classe Nazgul - Spectres de l'Anneau
    """

    def __init__(self, nom, dangerosite, monture):
        """
        Attribut supplémentaire:
        - monture (str): cheval noir ou créature ailée
        """
        super().__init__(nom, dangerosite)
        self.__monture = monture

    def attaquer(self):
        """
        Attaque avec cri spectral et lame maudite
        """
        degats = random.randint(1, self.dangerosite * 8)
        attaque = random.choice(["cri spectral", "lame maudite", "aura de terreur"])

        if 8 >= degats:
            print(f"{self.nom} rate son attaque et sa {self.__monture} panique, le désarçonnant pour {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} sur sa {self.__monture} utilise {attaque} et inflige {degats} points de dégâts de terreur")

    def decrire(self):
        """
        Retourne une description complète du Nazgûl
        """
        return f"Nazgûl {self.nom}: dangerosité {self.dangerosite}, chevauche {self.__monture}"


class Orque(CreatureMagique):
    """
    Classe Orque - serviteurs de Sauron
    """

    def __init__(self, nom, dangerosite, tribu):
        """
        Attribut supplémentaire:
        - tribu (str): Moria, Mordor, Isengard, etc.
        """
        super().__init__(nom, dangerosite)
        self.__tribu = tribu

    def attaquer(self):
        """
        Attaque brutale et sauvage
        """
        degats = random.randint(1, self.dangerosite * 5)
        arme = random.choice(["cimeterre", "hache", "arc"])

        if 5 >= degats:
            print(f"{self.nom} de {self.__tribu} se blesse avec son {arme} et subit {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} de {self.__tribu} charge avec son {arme} et inflige {degats} points de dégâts")

    def decrire(self):
        """
        Retourne une description complète de l'Orque
        """
        return f"Orque {self.nom} de {self.__tribu}: dangerosité {self.dangerosite}"


class Ent(CreatureMagique):
    """
    Classe Ent - bergers d'arbres
    """

    def __init__(self, nom, dangerosite, foret):
        """
        Attribut supplémentaire:
        - foret (str): forêt d'origine
        """
        super().__init__(nom, dangerosite)
        self.__foret = foret

    def attaquer(self):
        """
        Attaque lente mais puissante
        """
        degats = random.randint(1, self.dangerosite * 15)
        attaque = random.choice(["branches puissantes", "racines fouetteuses", "pierre lancée"])

        if 12 >= degats:
            print(f"{self.nom} trébuche avec ses racines et subit {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} de {self.__foret} frappe avec ses {attaque} et inflige {degats} points de dégâts")

    def decrire(self):
        """
        Retourne une description complète de l'Ent
        """
        return f"Ent {self.nom} gardien de {self.__foret}: dangerosité {self.dangerosite}"


class Araignee(CreatureMagique):
    """
    Classe Araignée - descendantes d'Ungoliant (comme Shelob)
    """

    def __init__(self, nom, dangerosite, venin):
        """
        Attribut supplémentaire:
        - venin (str): type de venin
        """
        super().__init__(nom, dangerosite)
        self.__venin = venin

    def attaquer(self):
        """
        Attaque avec morsure venimeuse et toile
        """
        degats = random.randint(1, self.dangerosite * 9)
        attaque = random.choice(["morsure venimeuse", "toile paralysante", "pattes acérées"])

        if 7 >= degats:
            print(f"{self.nom} s'empêtre dans sa propre toile et subit {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} utilise {attaque} avec son venin {self.__venin} et inflige {degats} points de dégâts")

    def decrire(self):
        """
        Retourne une description complète de l'Araignée
        """
        return f"Araignée {self.nom}: dangerosité {self.dangerosite}, venin {self.__venin}"


class Troll(CreatureMagique):
    """
    Classe Troll - créatures massives et stupides
    """

    def __init__(self, nom, dangerosite, type_troll):
        """
        Attribut supplémentaire:
        - type_troll (str): des cavernes, des montagnes, de pierre, etc.
        """
        super().__init__(nom, dangerosite)
        self.__type_troll = type_troll

    def attaquer(self):
        """
        Attaque brutale et désordonnée
        """
        degats = random.randint(1, self.dangerosite * 11)
        attaque = random.choice(["massue géante", "poings", "rocher lancé"])

        if 9 >= degats:
            print(f"{self.nom} le troll {self.__type_troll} se cogne la tête contre un mur et subit {degats} points de dégâts. Cause : échec critique")
        else:
            print(f"{self.nom} le troll {self.__type_troll} frappe avec {attaque} et inflige {degats} points de dégâts")

    def decrire(self):
        """
        Retourne une description complète du Troll
        """
        return f"Troll {self.__type_troll} {self.nom}: dangerosité {self.dangerosite}"


class Bestiaire:
    """
    Classe qui gère un ensemble de créatures magiques
    """

    def __init__(self):
        """
        Attribut:
        - creatures (liste)
        """
        self.__creatures = []

    def ajouter_creature(self, creature):
        """
        Ajoute une créature au bestiaire
        Vérifie que c'est bien une instance de CreatureMagique
        """
        if isinstance(creature, CreatureMagique):
            self.__creatures.append(creature)
        else:
            raise TypeError("Doit être une instance de CreatureMagique")

    def afficher_creatures(self):
        """
        Affiche la description de toutes les créatures
        """
        for creature in self.__creatures:
            print(creature.decrire())

    def attaque_generale(self):
        """
        Toutes les créatures attaquent
        """
        for creature in self.__creatures:
            creature.attaquer()

class Boromir(CreatureMagique):
    """
    Classe Boromir - Homme du Gondor, capitaine valeureux mais maudit
    """

    def __init__(self, nom, dangerosite, arme):
        """
        Attribut supplémentaire:
        - arme (str): épée, cor du Gondor, etc.
        """
        super().__init__(nom, dangerosite)
        self.__arme = arme

    def attaquer(self):
        """
        Attaque courageuse mais souvent fatale
        95% de chances de mourir en attaquant (percé de flèches)
        5% de chances d'attaque normale
        """
        mort = random.random()  # Génère un nombre entre 0 et 1

        if mort <= 0.95:  # 95% de chances
            print(f"💀 {self.nom} charge vaillamment mais est percé par trois flèches d'orques!")
            print(f"   '{self.nom}: J'aurais suivi mon capitaine... mon frère... mon roi.'")
            print(f"   {self.nom} est MORT en tentant de protéger les hobbits. RIP 🪦")
        else:  # 5% de chances de survie
            degats = random.randint(1, self.dangerosite * 7)
            attaque = random.choice(["épée du Gondor", self.__arme, "cor du Gondor"])

            if 6 >= degats:
                print(f"{self.nom} trébuche sur son bouclier et subit {degats} points de dégâts. Cause : échec critique")
            else:
                print(f"⚔️ {self.nom} se bat avec {attaque} et inflige {degats} points de dégâts!")
                print(f"   (Miracle! Boromir a survécu cette fois...)")

    def decrire(self):
        return f"Homme du Gondor {self.nom}: dangerosité {self.dangerosite}, armé de {self.__arme}"

if __name__ == "__main__":
    # NE PAS MODIFIER CE CODE DE TEST

    # Créatures originales
    dragon = Dragon("Smaug", 9, "rouge")
    elfe = Elfe("Legolas", 4, "Sylvestre")

    # Nouvelles créatures LOTR
    balrog = Balrog("Durin's Bane", 10, "fouet enflammé")
    nazgul = Nazgul("Witch-king d'Angmar", 9, "créature ailée")
    orque = Orque("Uglúk", 5, "Isengard")
    ent = Ent("Sylvebarbe", 7, "Fangorn")
    araignee = Araignee("Shelob", 8, "paralysant")
    troll = Troll("Grimbold", 6, "des cavernes")

    # Création du bestiaire
    bestiaire = Bestiaire()
    bestiaire.ajouter_creature(dragon)
    bestiaire.ajouter_creature(elfe)
    bestiaire.ajouter_creature(balrog)
    bestiaire.ajouter_creature(nazgul)
    bestiaire.ajouter_creature(orque)
    bestiaire.ajouter_creature(ent)
    bestiaire.ajouter_creature(araignee)
    bestiaire.ajouter_creature(troll)

    print("\n=== BESTIAIRE DE LA TERRE DU MILIEU ===")
    print("\n--- Créatures enregistrées ---")
    bestiaire.afficher_creatures()

    print("\n--- Attaques individuelles ---")
    dragon.attaquer()
    elfe.attaquer()
    balrog.attaquer()
    nazgul.attaquer()

    print("\n--- Attaque générale ! ---")
    bestiaire.attaque_generale()

    # Ajouter Boromir
    boromir = Boromir("Boromir fils de Denethor", 6, "épée et bouclier")

    # Création du bestiaire
    bestiaire = Bestiaire()
    # ... (ajouts existants)
    bestiaire.ajouter_creature(boromir)

    # ... (reste du code)

    print("\n--- Test spécial Boromir (va-t-il survivre?) ---")
    for i in range(1):
        print(f"\nTentative {i+1}:")
        boromir.attaquer()
