# Importation des modules nécessaires
from view.view_mainmenu import reports_main_menu_view


class Reports_Controller:
    # Initialisation du contrôleur avec les contrôleurs des tournois, joueurs et matchs comme paramètres
    def __init__(self, tournament_controller, player_controller, matches_controller):
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller
        self.reports_view = reports_main_menu_view()
        self.matchs_controller = matches_controller

    # Méthode pour trouver un tournoi par son nom et afficher ses détails
    def find_tournament_and_display_details(self):
        tournament_name = input("Entrez le nom du tournoi pour afficher ses détails : ")
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            self.display_tournament_details(tournament)
        else:
            print("Tournoi non trouvé.")

    # Méthode pour gérer les choix de l'utilisateur dans le menu des rapports
    def viewchoice(self):
        while True:
            # Afficher le menu des rapports et obtenir le choix de l'utilisateur
            choix = self.reports_view.show_menu()
            if choix == "1":
                # Afficher tous les joueurs par ordre alphabétique
                self.display_players_alphabetically()
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input("Entrez le nom du fichier pour l'exportation (sans extension) : ")
                    self.export_players_alphabetically(f"{filename}.txt")
            elif choix == "2":
                # Afficher tous les tournois
                self.display_all_tournaments()
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input("Entrez le nom du fichier pour l'exportation (sans extension) : ")
                    self.export_all_tournaments(f"{filename}.txt")
            elif choix == "3":
                # Demander le nom du tournoi et afficher ses détails
                tournament_name = input("Entrez le nom du tournoi pour afficher ses détails : ")
                self.display_tournament_details(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input("Entrez le nom du fichier pour l'exportation (sans extension) : ")
                    self.export_tournament_details(tournament_name, f"{filename}.txt")
            elif choix == "4":
                # Demander le nom du tournoi et afficher ses joueurs par ordre alphabétique
                tournament_name = input("Entrez le nom du tournoi pour afficher ses joueurs : ")
                self.display_tournament_players_alphabetically(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input("Entrez le nom du fichier pour l'exportation (sans extension) : ")
                    self.export_tournament_players_alphabetically(tournament_name, f"{filename}.txt")
            elif choix == "5":
                # Demander le nom du tournoi et afficher les détails des tours et des matchs
                tournament_name = input("Entrez le nom du tournoi pour afficher les détails complets: ")
                self.display_tournament_rounds_and_matches(tournament_name)
                choice = input("Voulez-vous exporter ce rapport ? (y/n): ")
                if choice.lower() == "y":
                    filename = input("Entrez le nom du fichier pour l'exportation (sans extension) : ")
                    self.export_tournament_rounds_and_matches(tournament_name, f"{filename}.txt")
            elif choix == "6":
                print("Retour au menu principal.")
                break
            else:
                print("Choix non valide, veuillez réessayer.")

    # Affichage des joueurs par ordre alphabétique.
    def display_players_alphabetically(self):
        players = sorted(self.player_controller.players, key=lambda x: (x.last_name, x.first_name))
        print("Liste de tous les joueurs par ordre alphabétique :")
        for player in players:
            print(f"ID: {player.chess_id} - {player.first_name} {player.last_name}")

    # Affichage de tous les tournois.
    def display_all_tournaments(self):
        print("Liste de tous les tournois :")
        for tournament in self.tournament_controller.tournaments:
            print(
                f"Nom: {tournament.name}, Lieu: {tournament.location}, Date: {tournament.start_date} "
                f"- {tournament.end_date}, Description: {tournament.description} "
            )

    # Affichage des détails d'un tournoi spécifique.
    def display_tournament_details(self, tournament_name):
        tournament = next(
            (t for t in self.tournament_controller.tournaments if t.name == tournament_name),
            None,
        )
        if tournament:
            print(
                f"Nom: {tournament.name}, Lieu: {tournament.location}, Date: {tournament.start_date} "
                f"- {tournament.end_date}, Description: {tournament.description} "
            )
            return tournament
        else:
            print("Tournoi non trouvé.")
            return None

    # Affichage des joueurs d'un tournoi spécifique par ordre alphabétique.
    def display_tournament_players_alphabetically(self, tournament_name):
        tournament = next(
            (t for t in self.tournament_controller.tournaments if t.name == tournament_name),
            None,
        )
        if tournament:
            players = sorted(tournament.players, key=lambda x: (x.last_name, x.first_name))
            print(f"Joueurs du tournoi {tournament.name} par ordre alphabétique :")
            for player in players:
                print(f"{player.first_name} {player.last_name}")
            return tournament
        else:
            print("Tournoi non trouvé.")
            return None

    # Affichage des tours et des matchs d'un tournoi spécifique.
    def display_tournament_rounds_and_matches(self, tournament_name):
        tournament = next(
            (t for t in self.tournament_controller.tournaments if t.name == tournament_name),
            None,
        )
        if tournament:
            print(f"Détails du tournoi {tournament.name}:")
            print(f"Lieu: {tournament.location}, Date: {tournament.start_date} - {tournament.end_date}")
            print("Joueurs :")
            for player in tournament.players:
                print(f"{player.first_name} {player.last_name} - Score total: {player.score}")
            print("Rounds et Matchs :")
            for round in tournament.rounds:
                print(f"{round.name}:")
                for match in round.matchs:
                    player1_name = f"{match.player1.first_name} {match.player1.last_name}"
                    player2_name = f"{match.player2.first_name} {match.player2.last_name}"
                    print(f"Match: {player1_name} vs {player2_name}, Score: {match.score1} - {match.score2}")
            return tournament
        else:
            print("Tournoi non trouvé.")
            return None

    # Exportation des joueurs par ordre alphabétique dans un fichier.
    def export_players_alphabetically(self, filename="players.txt"):
        players = sorted(self.player_controller.players, key=lambda x: (x.last_name, x.first_name))
        with open(filename, "w", encoding="utf-8") as file:
            for player in players:
                file.write(
                    f"ID: {player.chess_id}, Nom: {player.first_name}, Prénom: {player.last_name}, "
                    f"Date de naissance: {player.birth_date}\n"
                )
        print(f"Les joueurs ont été exportés avec succès dans {filename}.")

    # Exportation de tous les tournois dans un fichier.
    def export_all_tournaments(self, filename="tournaments.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for tournament in self.tournament_controller.tournaments:
                file.write(
                    f"Name: {tournament.name}, Location: {tournament.location}, Start Date: {tournament.start_date}, "
                    f"End Date: {tournament.end_date},  Description: {tournament.description}\n"
                )
        print(f"Les tournois ont été exportés avec succès dans {filename}.")

    # Exportation des détails d'un tournoi spécifique dans un fichier.
    def export_tournament_details(self, tournament_name, filename):
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(
                    f"Name: {tournament.name}\nLocation: {tournament.location}\nStart Date: {tournament.start_date}\n "
                    f"End Date: {tournament.end_date}\nDescription: {tournament.description}\n"
                )
            print(f"Détails du tournoi '{tournament_name}' exportés avec succès dans {filename}.")
        else:
            print(f"Tournoi '{tournament_name}' non trouvé.")

    # Exportation des joueurs d'un tournoi spécifique par ordre alphabétique dans un fichier.
    def export_tournament_players_alphabetically(self, tournament_name, filename):
        tournament = self.matchs_controller.find_tournament_by_name(tournament_name)
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                for player in sorted(tournament.players, key=lambda x: (x.last_name, x.first_name)):
                    file.write(f"{player.first_name} {player.last_name}\n")
            print(f"Les joueurs du tournoi '{tournament_name}' ont été exportés avec succès dans {filename}.")
        else:
            print(f"Tournoi '{tournament_name}' non trouvé.")

    # Exportation des rounds et des matchs d'un tournoi spécifique dans un fichier.
    def export_tournament_rounds_and_matches(self, tournament_name, filename):
        tournament = next(
            (t for t in self.tournament_controller.tournaments if t.name == tournament_name),
            None,
        )
        if tournament:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Détails du tournoi {tournament.name}:\n")
                file.write(f"Lieu: {tournament.location}, Date: {tournament.start_date} - {tournament.end_date}\n")
                file.write("Joueurs :\n")
                for player in tournament.players:
                    file.write(f"{player.first_name} {player.last_name} - Score total: {player.score}\n")
                file.write("Rounds et Matchs :\n")
                for round in tournament.rounds:
                    file.write(f"{round.name}:\n")
                    for match in round.matchs:
                        player1 = f"{match.player1.first_name} {match.player1.last_name}"
                        player2 = f"{match.player2.first_name} {match.player2.last_name}"
                        file.write(f"Match: {player1} vs {player2}, Score: {match.score1} - {match.score2}\n")
            print(f"Détails du tournoi '{tournament_name}' exportés avec succès dans {filename}.")
        else:
            print("Tournoi non trouvé.")
