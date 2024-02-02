# from controller.controller_main import Main_controller
# from controller.controller_players import Player_Controller
# from controller.controller_tournaments import Tournament_Controller
# from controller.controller_matchs import Match_Controller

# from view.xxxxxxx import menu_view_imput   xxxxxxxxxxxxxxxx


class main_menu_view:
    def show_menu(self):
        """
        Affiche le menu principal
        """
        print("\nMenu Principal")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Quitter")
        choix = input("Entrez le numéro de votre choix : ")
        return choix


class player_main_menu_view:
    def show_menu(self):
        """
        Affiche le menu de la gestion des joueurs
        """
        print("\nMenu de la Gestion des Joueurs")
        print("1. Ajouter un nouveau joueur")
        print("2. Mettre à jour un joueur existant")
        print("3. Supprimer un joueur")
        print("4. Afficher tous les joueurs")
        print("5. Afficher les joueurs par score")
        print("6. Afficher les joueurs par ordre alphabétique")
        print("7. Retourner au menu principal")
        print("8. Quitter")

        choix = input("Entrez le numéro de votre choix : ")
        return choix


# gestion tournois !

# autre

# a completer
