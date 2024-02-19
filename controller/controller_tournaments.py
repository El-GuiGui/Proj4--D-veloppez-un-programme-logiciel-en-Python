import random
from model.model_tournaments import Tournament, Round, Match
from view.view_mainmenu import tournament_main_menu_view
from view.view_tournaments import tournaments_view


# ajouter fonction quitter dans tous les sous-menus .....
# ajouter fonction de désinscrire un joueurs a tout moment d'un tournois
# rgler round et match
# regler show result (aussi dans model tournament)
# reprendre tournois a modifier et arreter tournois


class Tournament_Controller:
    def __init__(self, player_controller):
        self.tournaments = []
        self.player_controller = player_controller
        self.view = tournament_main_menu_view()
        self.details_view = tournaments_view()

    def viewchoice(self):
        while True:
            choix = self.view.show_menu()
            if choix == "1":
                self.create_tournament()
            elif choix == "2":
                self.show_tournament_details()
            elif choix == "3":
                self.list_tournaments()
            elif choix == "4":
                self.resume_tournaments
            elif choix == "5":
                break
            else:
                print("Choix non valide, réessayer !")

    def manage_tournament(self, tournament):
        while True:
            choix = self.view.show_manage_tournament_menu()
            if choix == "1":
                self.register_players(tournament)
            elif choix == "2":
                self.start_next_round(tournament)
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
        new_tournament = Tournament(*details)
        self.tournaments.append(new_tournament)
        print("Tournoi créé avec succès. Passons a la gestion du tournois.")
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

    def start_next_round(self, tournament):
        try:
            new_round = tournament.start_new_round()
            print(f"{new_round.name} a commencé.")
        except ValueError as e:
            print(e)

    def show_current_results(self, tournament):
        print("Résultats actuels du tournoi :")
        # a modifier

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
