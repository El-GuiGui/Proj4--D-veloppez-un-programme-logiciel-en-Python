from model.model_players import players

# from view.view_players import Player_View
from view.view_mainmenu import player_main_menu_view


class Player_Controller:
    def __init__(self):
        self.players = []
        self.player_menu_view = player_main_menu_view()

    def viewchoice(self):
        while True:
            choix = self.player_menu_view.show_menu()
            if choix == "1":
                self.create_player()
            elif choix == "2":
                self.update_player()
            elif choix == "3":
                self.delete_player()
            elif choix == "4":
                self.show_all_players()
            elif choix == "5":
                self.show_players_by_score()
            elif choix == "6":
                self.show_players_alphabetically()
            elif choix == "7":
                print("Retour au menu principal.")
            elif choix == "8":
                print("Fermeture du programme.")
                break
            else:
                print("Choix non valide, réessayer !")
        pass

    def create_player(self):
        details = self.view.get_player_details()
        new_player = players(*details)
        self.players.append(new_player)
        print("Ajout d'un nouveau joueur réussi !")

    def update_player(self, player):
        # maj joueur
        updated_player = self.view.update_player_details(player)

    def show_all_players(self):
        self.view.show_players_list(self.players)


# delete player, show  player by score,
