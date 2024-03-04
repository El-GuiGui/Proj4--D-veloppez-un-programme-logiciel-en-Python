from model.model_tournaments import Tournament
from model.model_players import players
from view.view_mainmenu import reports_main_menu_view
from controller.controller_matchs import MatchsController


class Reports_Controller:
    def __init__(self, tournament_controller, player_controller):
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller
        self.reports_view = reports_main_menu_view()
        self.matchs_controller = MatchsController

    def viewchoice(self):
        while True:
            choix = self.reports_view.show_menu()
            if choix == "1":
                self.display_players_alphabetically()
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input(
                        "Entrez le nom du fichier pour l'exportation (sans extension) : "
                    )
                    self.export_players_alphabetically(f"{filename}.txt")
            elif choix == "2":
                self.display_all_tournaments()
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input(
                        "Entrez le nom du fichier pour l'exportation (sans extension) : "
                    )
                    self.export_all_tournaments(f"{filename}.txt")
            elif choix == "3":
                tournament_name = input(
                    "Entrez le nom du tournoi pour afficher ses détails : "
                )
                self.display_tournament_details(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input(
                        "Entrez le nom du fichier pour l'exportation (sans extension) : "
                    )
                    self.export_tournament_details(tournament_name, f"{filename}.txt")
            elif choix == "4":
                tournament_name = input(
                    "Entrez le nom du tournoi pour afficher ses détails : "
                )
                self.display_tournament_players_alphabetically(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input(
                        "Entrez le nom du fichier pour l'exportation (sans extension) : "
                    )
                    self.export_tournament_players_alphabetically(f"{filename}.txt")
            elif choix == "5":
                tournament_name = input(
                    "Entrez le nom du tournoi pour afficher ses détails : "
                )
                self.display_tournament_rounds_and_matches(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input(
                        "Entrez le nom du fichier pour l'exportation (sans extension) : "
                    )
                    self.export_tournament_rounds_and_matches(f"{filename}.txt")
            elif choix == "6":
                tournament_name = input(
                    "Entrez le nom du tournoi pour afficher ses détails : "
                )
                print("Retour au menu principal.")
                break
            else:
                print("Choix non valide, veuillez réessayer.")

    def display_players_alphabetically(self):
        players = sorted(
            self.player_controller.players, key=lambda x: (x.last_name, x.first_name)
        )
        print("Liste de tous les joueurs par ordre alphabétique :")
        for player in players:
            print(
                f"{player.first_name} {player.last_name}, Rank: {player.rank}, Score: {player.score}"
            )

    def display_all_tournaments(self):
        print("Liste de tous les tournois :")
        for tournament in self.tournament_controller.tournaments:
            print(
                f"Nom: {tournament.name}, Lieu: {tournament.location}, Date: {tournament.start_date} - {tournament.end_date}"
            )

    def display_tournament_details(self, tournament_name):
        tournament = next(
            (
                t
                for t in self.tournament_controller.tournaments
                if t.name == tournament_name
            ),
            None,
        )
        if tournament:
            print(f"Détails du tournoi {tournament.name}:")
            print(
                f"Lieu: {tournament.location}, Date: {tournament.start_date} - {tournament.end_date}"
            )
            print("Joueurs :")
            for player in tournament.players:
                print(f"{player.first_name} {player.last_name}")
            print("Rounds et Matchs :")
            for round in tournament.rounds:
                print(f"{round.name}:")
                for match in round.matches:
                    print(
                        f"Match: {match.player1} vs {match.player2}, Score: {match.score1} - {match.score2}"
                    )
        else:
            print("Tournoi non trouvé.")

    def display_tournament_players_alphabetically(self, tournament_name):
        tournament = next(
            (
                t
                for t in self.tournament_controller.tournaments
                if t.name == tournament_name
            ),
            None,
        )
        if tournament:
            players = sorted(
                tournament.players, key=lambda x: (x.last_name, x.first_name)
            )
            print(f"Joueurs du tournoi {tournament.name} par ordre alphabétique :")
            for player in players:
                print(f"{player.first_name} {player.last_name}")
        else:
            print("Tournoi non trouvé.")

    def display_tournament_rounds_and_matches(self, tournament_name):
        tournament = next(
            (
                t
                for t in self.tournament_controller.tournaments
                if t.name == tournament_name
            ),
            None,
        )
        if tournament:
            print(f"Tours et matchs du tournoi {tournament.name} :")
            for round in tournament.rounds:
                print(f"{round.name}:")
                for match in round.matches:
                    print(
                        f"Match: {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}, Score: {match.score1} - {match.score2}"
                    )
        else:
            print("Tournoi non trouvé.")

    def export_players_alphabetically(self, filename="players.txt"):
        players = sorted(
            self.player_controller.players, key=lambda x: (x.last_name, x.first_name)
        )
        with open(filename, "w", encoding="utf-8") as file:
            for player in players:
                file.write(
                    f"ID: {player.chess_id}, Nom: {player.first_name} {player.last_name}, Date de naissance: {player.birth_date}, Score: {player.score}\n"
                )
        print(f"Les joueurs ont été exportés avec succès dans {filename}.")

    def export_all_tournaments(self, filename="tournaments.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for tournament in self.tournament_controller.tournaments:
                file.write(
                    f"Name: {tournament.name}, Location: {tournament.location}, Start Date: {tournament.start_date}, End Date: {tournament.end_date}\n"
                )
        print(f"Les tournois ont été exportés avec succès dans {filename}.")

    def export_tournament_details(
        self, tournament_name, filename="tournament_details.txt"
    ):
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(
                    f"Name: {tournament.name}\nLocation: {tournament.location}\nStart Date: {tournament.start_date}\nEnd Date: {tournament.end_date}\n"
                )
                file.write("Players:\n")
                for player in sorted(
                    tournament.players, key=lambda x: (x.last_name, x.first_name)
                ):
                    file.write(f"  {player.first_name} {player.last_name}\n")
                file.write("Rounds:\n")
                for round in tournament.rounds:
                    file.write(f"  {round.name}\n")
                    for match in round.matches:
                        file.write(
                            f"    {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}\n"
                        )
            print(
                f"Détails du tournoi '{tournament_name}' exportés avec succès dans {filename}."
            )
        else:
            print(f"Tournoi '{tournament_name}' non trouvé.")

    def export_tournament_players_alphabetically(
        self, tournament_name, filename="tournament_players.txt"
    ):
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                for player in sorted(
                    tournament.players, key=lambda x: (x.last_name, x.first_name)
                ):
                    file.write(
                        f"{player.first_name} {player.last_name}, Rank: {player.rank}, Score: {player.score}\n"
                    )
            print(
                f"Les joueurs du tournoi '{tournament_name}' ont été exportés avec succès dans {filename}."
            )
        else:
            print(f"Tournoi '{tournament_name}' non trouvé.")

    def export_tournament_rounds_and_matches(
        self, tournament_name, filename="tournament_rounds_and_matches.txt"
    ):
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                for round in tournament.rounds:
                    file.write(f"Round: {round.name}\n")
                    for match in round.matches:
                        file.write(
                            f"  {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}, Score: {match.score1}-{match.score2}\n"
                        )
            print(
                f"Les rounds et les matchs du tournoi '{tournament_name}' ont été exportés avec succès dans {filename}."
            )
        else:
            print(f"Tournoi '{tournament_name}' non trouvé.")
