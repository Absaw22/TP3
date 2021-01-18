# -*- coding: utf-8 -*-
"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Dois être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une partie et
utilise un objet tableau_mines (une instance de la classe Tableau).

Auteurs: à compléter
"""

from tableau import Tableau


class Partie(Tableau):
    """
    Contient les informations sur une partie du jeu Démineur, qui se jouera avec
    un tableau de mines. Des méthodes sont disponibles pour faire avancer la partie 
    et interagir avec l'utilisateur.

    Attributes:
        tableau_mines (Tableau): Le tableau de cases où les mines sont cachées avec lequel se
                déroule la partie.
        partie_terminee (bool): True lorsque l'utilisateur a terminé de jouer la partie (victoire ou défaite)
    """

    def __init__(self):
        """
        Initialisation de la Partie. 
        
        Note: L'instance de la classe Tableau, qui sera manipulée par les méthodes de la classe,
              sera initialisée lors de l'appel de la méthode Partie.jouer().
        """
        self.tableau_mines = None
        self.partie_terminee = False

    def jouer(self):
        """
        Tant que la partie n'est pas terminée, on joue un tour de la partie. 
        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilée
        et on indique un message sur l'issue de la partie (victoire ou défaite).
        """
        
        ### TODO: Modifier le code pour demander à l'utilisateur de choisir la taille
        ### du tableau (nombre de lignes et nombres de colonnes, ainsi que le nombre 
        ### de mines)  
        
        #Lancement de la partie en demandant les configurations du tableau 
        dimension_rangee = int(input("Entrez un nombre de rangee: "))
        dimension_colonne = int(input("Entrez un nombre de colonne: "))
        nombres_mines = int(input("Entrez un nombre de mines: "))
                  
        self.tableau_mines = Tableau(dimension_rangee, dimension_colonne, nombres_mines)
        
        #On entre dans la boucle des tours pour la partie
        compteur_tours = 0
        while not self.partie_terminee: 
                   
            compteur_tours += 1
            print(f'\n===> Tour #{compteur_tours} <===')
            self.tableau_mines.afficher_tableau()
            self.tour()

        self.tableau_mines.afficher_solution()    
        #Affichage du message de victoire ou de défaite
        if self.tableau_mines.nombre_cases_sans_mine_a_devoiler == 0:
            print("Bravo, vous avez gagné!")
            
        else:
            print("Vous avez perdu!")
            self.tableau_mines.afficher_solution()

    def tour(self):
        """ 
        Jouer un tour, c'est-à-dire:
        
        À chaque tour:
            - On demande à l'utilisateur les coordonnées d'une case à dévoiler
            - On dévoile la case
            - On détecte si une mine a été actionnée, 
              auquel cas affecte True à l'attribut self.partie_terminee.
            - On détecte si toutes les cases ont été dévoilées, 
              auquel cas affecte True à l'attribut self.partie_terminee.
        """
        

        #Début de chaque tour, tant que la partie n'est pas fini
        print("Entrez les coordonnées d'une case à dévoiler:")
        rangee_x = int(input("Entrez la coordonnée X: "))
        colonne_y = int(input("Entrez la coordonnée Y: "))
        self.tableau_mines.devoiler_case(rangee_x,colonne_y)
        
        #Détection de fin de partie
        if self.tableau_mines.contient_mine(rangee_x, colonne_y) == True:
            return self.partie_terminee == True
        elif self.tableau_mines.contient_cases_a_devoiler == False:
            return self.partie_terminee == True

    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Méthode qui valide les coordonnées reçues en paramètres.
        Les coordonnées doivent:
            1) être des caractères numériques;
            2) être à l'intérieur des valeurs possibles des rangées et des colonnes 
                du tableau; et 
            3) correspondre à une case qui n'a pas encore été dévoilée.

        Args:
            rangee_x (str):     Chaîne de caractères contenant la rangée
            colonne_y (str):    Chaîne de caractères contenant  la colonne

        Returns:
            bool : True si les coordonnées sont valides, False autrement.
        """

    
        
        
        
        coordonnees_a_valider = False
        while coordonnees_a_valider:
            

            if self.tableau_mines.valider_coordonnees_a_devoiler(rangee_x, colonne_y) == True:
                 
                return coordonnees_a_valider == True
                 
            else:
                return False  



        """
        Méthode qui demande à l'utilisateur d'entrer la coordonnée de la case qu'il veut dévoiler.
        Cette coordonnée comporte un numéro de rangée et un numéro de colonne.
        Tant que les coordonnées ne sont pas valides, on redemande de nouvelles coordonnées.
        Une fois les coordonnées validées, on retourne les deux numéros sous forme d'entiers.

        Returns:
            int: Numéro de la rangée
            int: Numéro de la colonne

        """ 
        coordonnees_valides = False
        while coordonnees_valides == False :
            num_rangée = input('Entrez la rangée de la case a dévoiler : ')
            num_colonne = input('Entrez la colonne de la case a dévoiler : ')

            if self.valider_coordonnees(num_rangée, num_colonne):
                coordonnees_valides = True
                return int(num_rangée) , int(num_colonne)  

            else:
              print ('Coordonnées non valides, reéssayez')


