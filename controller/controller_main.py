# Importation des modules nécessaires
from view.view_mainmenu import main_menu_view
from controller.controller_players import Player_Controller
from controller.controller_tournaments import Tournament_Controller
from controller.controller_reports import Reports_Controller
from controller.controller_matchs import MatchsController


class Main_controller:
    def __init__(self):
        # Initialisation de l'interface principale de l'utilisateur.
        self.main_menu_view = main_menu_view()
        # Initialisation du contrôleur gérant les joueurs.
        self.player_controller = Player_Controller()
        # Initialisation du contrôleur gérant les tournois
        self.tournament_controller = Tournament_Controller(self.player_controller)
        # Initialisation du contrôleur gérant les matchs
        self.matches_controller = MatchsController(self.tournament_controller)
        # Initialisation du contrôleur gérant les rapports.
        self.reports_controller = Reports_Controller(
            self.tournament_controller, self.player_controller, self.matches_controller
        )

    def run(self):
        # Exécution du menu principal de l'application.
        while True:
            choix = self.main_menu_view.show_menu()
            # Gestion du choix de l'utilisateur.
            if choix == "1":
                # Redirection vers le contrôleur des joueurs.
                self.player_controller.viewchoice()
            elif choix == "2":
                # Redirection vers le contrôleur des tournois.
                self.tournament_controller.viewchoice()
            elif choix == "3":
                # Redirection vers le contrôleur des rapports.
                self.reports_controller.viewchoice()
            elif choix == "4":
                # Fermeture de l'application.
                print("Fermeture du programme.")
                break
            else:
                print("Choix non valide, réessayer !")
        pass
