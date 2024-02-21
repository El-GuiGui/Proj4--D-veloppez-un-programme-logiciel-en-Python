import json
from model.model_players import players
from model.model_tournaments import Tournament, Round, Match
from view.view_mainmenu import tournament_main_menu_view
from view.view_tournaments import tournaments_view
from controller.controller_matchs import MatchsController

# ajouter fonction quitter dans tous les sous-menus .....
# ajouter fonction de désinscrire un joueurs a tout moment d'un tournois
# rgler round et match


class Tournament_Controller:
    def __init__(self, player_controller):
        self.tournaments = self.load_tournaments()
        self.player_controller = player_controller
        self.view = tournament_main_menu_view()
        self.details_view = tournaments_view()
        self.matches_controller = MatchsController(self)

    def load_tournaments(self):
        try:
            with open("data_json/tournaments.json", "r") as file:
                tournaments_data = json.load(file)["tournaments"]
                loaded_tournaments = []
                for tournament_data in tournaments_data:
                    player_instances = [
                        players.players_deserialize(player_data)
                        for player_data in tournament_data["players"]
                    ]
                    tournament_data["players"] = player_instances
                    loaded_tournaments.append(Tournament(**tournament_data))
                return loaded_tournaments
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tournaments(self):
        with open("data_json/tournaments.json", "w") as file:
            tournaments_data = [
                tournament.tournament_serialize() for tournament in self.tournaments
            ]
            json.dump({"tournaments": tournaments_data}, file, indent=4)

    def viewchoice(self):
        """
        Input pour le menu des tournois

        """
        while True:
            choix = self.view.show_menu()
            if choix == "1":
                self.create_tournament()
            elif choix == "2":
                self.show_tournament_details()
            elif choix == "3":
                self.list_tournaments()
            elif choix == "4":
                self.resume_tournaments()
            elif choix == "5":
                break
            else:
                print("Choix non valide, réessayer !")

    def manage_tournament(self, tournament):
        """
        Input pour le menu de la gestion d'un tournois

        """
        while True:
            choix = self.view.show_manage_tournament_menu()
            if choix == "1":
                self.register_players(tournament)
            elif choix == "2":
                self.start_round(tournament)
            elif choix == "3":
                self.show_current_results(tournament)
            elif choix == "4":
                self.generate_player_pairs(tournament)
            elif choix == "5":
                break  # Retour au menu des tournois
            else:
                print("Choix non valide, réessayer !")

    """
    Option premier menu
    """

    def create_tournament(self):
        details = self.details_view.get_tournament_details()
        new_tournament = Tournament(**details)
        self.tournaments.append(new_tournament)
        self.save_tournaments()
        print("Tournoi créé avec succès. Passons a la gestion de ce tournois.")
        self.manage_tournament(new_tournament)

    def show_tournament_details(self):
        tournament_name = input("Entrez le nom du tournoi : ")
        found = False
        for tournament in self.tournaments:
            if tournament.name.lower() == tournament_name.lower():
                self.view.show_tournament_details(tournament)
                found = True
                break
        if not found:
            print("Tournoi non trouvé.")

    def list_tournaments(self):
        if not self.tournaments:
            print("Aucun tournoi disponible.")
        else:
            for tournament in self.tournaments:
                print(
                    f"Nom : {tournament.name}, Lieu : {tournament.location}, Dates : {tournament.start_date} à {tournament.end_date}"
                )

    def resume_tournaments(self):
        # Afficher tous les tournois disponibles.
        if not self.tournaments:
            print("Aucun tournoi disponible pour reprendre.")
            return

        print("Tournois disponibles pour reprendre :")
        for index, tournament in enumerate(self.tournaments, start=1):
            print(f"{index}. {tournament.name} - {tournament.location}")

        # Choix du tournois à reprendre
        choice = input("Entrez le numéro du tournoi à reprendre : ")
        try:
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(self.tournaments):
                selected_tournament = self.tournaments[selected_index]
                print(f"Reprise du tournoi: {selected_tournament.name}")
                self.manage_tournament(selected_tournament)
            else:
                print("Sélection invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    """
    Option deuxième menu
    """

    def register_players(self, tournament):
        print("Inscription des joueurs au tournoi.")
        players = self.player_controller.get_players()
        for player in players:
            print(f"{player.chess_id}: {player.first_name} {player.last_name}")
        while True:
            player_id = input(
                "Entrez l'identifiant d'échecs du joueur à inscrire (ou 'fin' pour terminer) : "
            )
            if player_id.lower() == "fin":
                break
            # Trouver et inscrire le joueur par son ID
            player = next((p for p in players if p.chess_id == player_id), None)
            if player:
                tournament.add_player(player)
                print(f"Joueur {player.first_name} {player.last_name} inscrit.")
            else:
                print("Joueur non trouvé.")
            self.save_tournaments()

    def start_round(self, tournament_name, round_name):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            try:
                new_round = tournament.start_new_round(round_name)
                print(f"Round {new_round.name} démarré.")
                self.save_tournaments()  # Assurez-vous que cette méthode sauvegarde l'état actuel des tournois dans un fichier JSON
            except ValueError as e:
                print(e)
        else:
            print("Tournoi introuvable.")

    def end_round(self, tournament_name, round_name):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round_to_end = next(
                (r for r in tournament.rounds if r.name == round_name), None
            )
            if round_to_end:
                round_to_end.end_round()
                print(f"Round {round_to_end.name} terminé.")
                self.save_tournaments()
            else:
                print("Round introuvable.")
        else:
            print("Tournoi introuvable.")

    def show_current_results(self, tournament):
        print("Résultats actuels du tournoi :")
        tournament.show_results()

    def generate_player_pairs(self, tournament):
        if len(tournament.players) % 2 != 0:
            print("Nombre impair de joueurs, impossible de générer des paires.")
            return

        # Trier les joueurs par score décroissant (ou croissant si souhaité)
        sorted_players = sorted(
            tournament.players, key=lambda player: player.score, reverse=True
        )

        # Générer des paires à partir de la liste triée
        for i in range(0, len(sorted_players), 2):
            print(
                f"Paire: {sorted_players[i].first_name} {sorted_players[i].last_name} (Score: {sorted_players[i].score}) "
                f"vs {sorted_players[i+1].first_name} {sorted_players[i+1].last_name} (Score: {sorted_players[i+1].score})"
            )
