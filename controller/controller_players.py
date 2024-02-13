from model.model_players import players

from view.view_players import Player_View
from view.view_mainmenu import player_main_menu_view


class Player_Controller:
    def __init__(self):
        self.players = []
        self.player_menu_view = player_main_menu_view()
        self.view = Player_View()

    # retourner la liste des joueurs
    def get_players(self):
        return self.players

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
                break
            elif choix == "8":
                print("Fermeture du programme.")
                exit()
            else:
                print("Choix non valide, réessayer !")
        pass

    def create_player(self):
        details = self.view.get_player_details()
        new_player = players(*details)
        self.players.append(new_player)
        print("Ajout d'un nouveau joueur réussi !")

    def update_player(self):
        chess_id = input("Entrez l'identifiant d'échecs du joueur à mettre à jour: ")
        # Trouver le joueur avec son identifiant national d'échecs
        player_to_update = next(
            (player for player in self.players if player.chess_id == chess_id), None
        )
        if player_to_update:
            self.view.update_player_details(player_to_update)
            print(
                f"Les détails du joueur {player_to_update.first_name} ont été mis à jour."
            )
        else:
            print("Aucun joueur trouvé avec cet identifiant d'échecs.")

    def delete_player(self):
        chess_id = input("Entrez l'identifiant d'échecs du joueur à supprimer : ")
        player_to_delete = next(
            (player for player in self.players if player.chess_id == chess_id), None
        )
        if player_to_delete:
            self.players.remove(player_to_delete)
            print(
                f"Le joueur {player_to_delete.first_name} {player_to_delete.last_name} a été supprimé."
            )
        else:
            print("Aucun joueur trouvé avec cet identifiant d'échecs.")

    def show_all_players(self):
        print(f"Nombre de joueurs enregistrés : {len(self.players)}")
        if not self.players:
            print("Il n'y a pas de joueurs à afficher.")
        else:
            self.view.show_players_list(self.players)

    def show_players_by_score(self):
        if not self.players:
            print("Il n'y a pas de joueurs à afficher.")
        else:
            self.view.show_players_by_score(self.players)

    def show_players_alphabetically(self):
        if not self.players:
            print("Il n'y a pas de joueurs à afficher.")
        else:
            self.view.show_players_alphabetically(self.players)
