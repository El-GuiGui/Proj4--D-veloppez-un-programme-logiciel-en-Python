from view.view_mainmenu import main_menu_view
from controller.controller_players import Player_Controller
from controller.controller_tournaments import Tournament_Controller


class Main_controller:
    def __init__(self):
        # Création d'une instance de MainMenuView
        self.main_menu_view = main_menu_view()
        # Création d'une instance de Player_Controller
        self.player_controller = Player_Controller()
        # Création d'une instance de Tournament_Controller
        self.tournament_controller = Tournament_Controller(self.player_controller)

    def run(self):
        while True:
            choix = self.main_menu_view.show_menu()
            if choix == "1":
                self.player_controller.viewchoice()
            elif choix == "2":
                self.tournament_controller.viewchoice()
            elif choix == "3":
                print("Fermeture du programme.")
                break
            else:
                print("Choix non valide, réessayer !")
        pass
