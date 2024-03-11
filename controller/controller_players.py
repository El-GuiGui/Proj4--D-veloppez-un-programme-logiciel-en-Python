# Importation des modules nécessaires
import json
import os
from model.model_players import players
from view.view_players import Player_View
from view.view_mainmenu import player_main_menu_view


class Player_Controller:
    def __init__(self):
        # Initialisation de la liste des joueurs et des vues.
        self.players = self.load_players()
        self.player_menu_view = player_main_menu_view()
        self.view = Player_View()

    # Chargement des joueurs depuis un fichier JSON.
    def load_players(self, file_path="data_json/players.json"):
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump({"players": []}, file)
            return []
        with open(file_path, "r") as file:
            data = json.load(file)
            return [players(**player_dict) for player_dict in data.get("players", [])]

    # Sauvegarde des joueurs dans un fichier JSON.
    def save_players(self, file_path="data_json/players.json"):
        with open(file_path, "w") as file:
            players_data = [player.players_serialize() for player in self.players]
            json.dump({"players": players_data}, file, indent=4)

    # Retourne la liste actuelle des joueurs.
    def get_players(self):
        return self.players

    # Gère les choix de l'utilisateur dans le menu des joueurs.
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
                self.show_players_alphabetically()
            elif choix == "6":
                print("Retour au menu principal.")
                break
            elif choix == "7":
                print("Fermeture du programme.")
                exit()
            else:
                print("Choix non valide, réessayer !")
        pass

    # Crée un nouveau joueur et l'ajoute à la liste.
    def create_player(self):
        details = self.view.get_player_details()
        new_player = players(**details)
        self.players.append(new_player)
        self.save_players()
        print("Ajout d'un nouveau joueur réussi !")

    # Met à jour les informations d'un joueur existant.
    def update_player(self):
        chess_id = input("Entrez l'identifiant d'échecs du joueur à mettre à jour: ")
        for player in self.players:
            if player.chess_id == chess_id:
                updated_info = self.view.get_player_details()
                player.first_name = updated_info.get("first_name", player.first_name)
                player.last_name = updated_info.get("last_name", player.last_name)
                player.birth_date = updated_info.get("birth_date", player.birth_date)
                player.chess_id = updated_info.get("chess_id", player.chess_id)
                player.score = updated_info.get("score", player.score)
                self.save_players()
                print(f"Les détails du joueur {player.first_name} {player.last_name} ont été mis à jour.")
                return
        print("Aucun joueur trouvé avec cet identifiant d'échecs.")

    # Supprime un joueur de la liste.
    def delete_player(self):
        chess_id = input("Entrez l'identifiant d'échecs du joueur à supprimer : ")
        player_to_delete = next((player for player in self.players if player.chess_id == chess_id), None)
        if player_to_delete:
            self.players.remove(player_to_delete)
            print(f"Le joueur {player_to_delete.first_name} {player_to_delete.last_name} a été supprimé.")
        else:
            print("Aucun joueur trouvé avec cet identifiant d'échecs.")
        self.save_players()

    # Affiche tous les joueurs.
    def show_all_players(self):
        print(f"Nombre de joueurs enregistrés : {len(self.players)}")
        if not self.players:
            print("Il n'y a pas de joueurs à afficher.")
        else:
            self.view.show_players_list(self.players)

    # Affiche les joueurs par ordre alphabétique.
    def show_players_alphabetically(self):
        if not self.players:
            print("Il n'y a pas de joueurs à afficher.")
        else:
            self.view.show_players_alphabetically(self.players)
