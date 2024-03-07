from view.view_mainmenu import main_menu_view
from controller.controller_players import Player_Controller
from controller.controller_tournaments import Tournament_Controller
from controller.controller_reports import Reports_Controller
from controller.controller_matchs import MatchsController


class Main_controller:
    def __init__(self):
        # Création d'une instance de MainMenuView
        self.main_menu_view = main_menu_view()
        # Création d'une instance de Player_Controller
        self.player_controller = Player_Controller()
        # Création d'une instance de Tournament_Controller
        self.tournament_controller = Tournament_Controller(self.player_controller)
        self.matches_controller = MatchsController(self.tournament_controller)
        # Création d'une instance de Reports_Controller
        self.reports_controller = Reports_Controller(
            self.tournament_controller, self.player_controller, self.matches_controller
        )

    def run(self):
        """
        Input pour le menu principal

        """
        while True:
            choix = self.main_menu_view.show_menu()
            if choix == "1":
                self.player_controller.viewchoice()
            elif choix == "2":
                self.tournament_controller.viewchoice()
            elif choix == "3":
                self.reports_controller.viewchoice()
            elif choix == "4":
                print("Fermeture du programme.")
                break
            else:
                print("Choix non valide, réessayer !")
        pass
