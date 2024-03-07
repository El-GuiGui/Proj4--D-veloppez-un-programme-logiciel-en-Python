import json
import random
from datetime import datetime
from model.model_matchs import Match
from model.model_players import players
from model.model_tournaments import Tournament, Round
from view.view_mainmenu import tournament_main_menu_view
from view.view_tournaments import tournaments_view
from controller.controller_matchs import MatchsController


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
                    rounds = [
                        self.convert_round_and_match(round_dict)
                        for round_dict in tournament_data.get("rounds", [])
                    ]
                    tournament_data["rounds"] = rounds
                    tournament_data["players"] = player_instances
                    loaded_tournaments.append(Tournament(**tournament_data))
                return loaded_tournaments
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tournaments(self):
        try:
            # Préparation des données pour la sauvegarde # Sauve des erreurs !
            tournaments_data = [
                tournament.tournament_serialize() for tournament in self.tournaments
            ]
            serialized_data = json.dumps({"tournaments": tournaments_data}, indent=4)
        except TypeError as e:
            print(f"Erreur lors de la sérialisation des données du tournoi: {e}")
            return

        try:
            with open("data_json/tournaments.json", "w") as file:
                file.write(serialized_data)
        except IOError as e:
            print(f"Erreur lors de l'écriture dans le fichier JSON: {e}")

    def convert_round_and_match(self, round_dict):
        new_round = Round(round_dict["name"])
        new_round.start_time = datetime.strptime(
            round_dict["start_time"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        new_round.end_time = (
            datetime.strptime(round_dict["end_time"], "%Y-%m-%dT%H:%M:%S.%f")
            if round_dict["end_time"]
            else None
        )
        new_round.matches = [
            Match(match["player1"], match["player2"]) for match in round_dict["matches"]
        ]
        new_round.is_finished = round_dict.get("is_finished", False)
        return new_round

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
                self.end_current_round(tournament)
            elif choix == "4":
                self.show_current_results(tournament)
            elif choix == "5":
                self.save_tournaments()
                print("Sauvegarde du tournoi actuel. Retour au menu des tournois.")
                break
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
                self.details_view.show_tournament_details(tournament)
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
                    f"Nom : {tournament.name}, Lieu : {tournament.location}, Dates : {tournament.start_date} à {tournament.end_date}, Description: {tournament.description}"
                )

    def resume_tournaments(self):
        # Afficher tous les tournois disponibles.
        if not self.tournaments:
            print("Aucun tournoi disponible.")
            return

        print("Tournois disponibles :")
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
        """
        Enregistrer les joueurs dans le tournoi

        """
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

    def start_round(self, tournament):
        """
        Démarrer un nouveau round dans le tournoi.

        """
        if tournament.current_round >= tournament.number_of_rounds:
            # Vérification du nombre de rounds par rapport à la valeur maximale
            print("Le nombre maximal de rounds pour ce tournoi a été atteint.")
            return

        print(f"Rounds actuels: {len(tournament.rounds)}")

        if tournament.current_round > 0 and len(tournament.rounds) > 0:
            # Vérification si le round précédent a bien été terminé
            last_round = tournament.rounds[tournament.current_round - 1]
            if not last_round.is_finished:
                print(
                    "Vous devez d'abord terminer le round en cours avant de commencer un nouveau."
                )
                return
        elif tournament.current_round == 0:
            # C'est le premier round, donc pas de round précédent à vérifier
            print("C'est le début du tournoi, aucun round précédent à vérifier.")
        else:
            # S'il y a une autre condition qui n'est pas respectée
            print("Il semble y avoir une erreur avec les rounds du tournoi.")
            return

        if tournament.current_round == 0:
            # Premier round, mélanger les joueurs aléatoirement
            shuffled_players = random.sample(
                tournament.players, len(tournament.players)
            )
            # Apparier les joueurs
            pairs = list(zip(shuffled_players[::2], shuffled_players[1::2]))
        else:
            # Rounds suivants, appairer les joueurs par score
            sorted_players = sorted(
                tournament.players, key=lambda x: x.score, reverse=True
            )
            pairs = []
            for i in range(0, len(sorted_players), 2):
                # Assurez-vous de ne pas appairer des joueurs déjà rencontrés si nécessaire
                pairs.append((sorted_players[i], sorted_players[i + 1]))

        if len(tournament.players) % 2 != 0:
            print(
                "Le nombre de joueurs est impair, impossible de générer des paires de matchs."
            )
            return

        # Créer un nouvel objet Round
        round_name = f"Round {tournament.current_round + 1}"
        new_round = Round(round_name)
        for pair in pairs:
            # Créer et ajouter un match pour chaque paire de joueurs
            match = Match(pair[0], pair[1])
            new_round.add_match(match)

        tournament.rounds.append(new_round)
        tournament.current_round += 1
        self.save_tournaments()
        print(f"Le round {tournament.current_round} a commencé.")
        # Afficher les paires pour ce round
        for index, match in enumerate(new_round.matchs):
            print(
                f"Match {index + 1}: {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}"
            )

    def end_current_round(self, tournament):
        """
        Demande les scores pour chaque match du round actuel et met à jour les scores.

        """
        if tournament.current_round == 0 or tournament.current_round > len(
            tournament.rounds
        ):
            print("Aucun round en cours à terminer.")
            return

        # Obtenez le round actuel
        current_round = tournament.rounds[tournament.current_round - 1]
        match_results = []

        # Demandez les scores pour chaque match
        for i, match in enumerate(current_round.matchs, start=1):
            print(
                f"Match {i}: {match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name}"
            )
            score1 = float(
                input(
                    f"Entrez le score pour {match.player1.first_name} {match.player1.last_name}: "
                )
            )
            score2 = float(
                input(
                    f"Entrez le score pour {match.player2.first_name} {match.player2.last_name}: "
                )
            )
            match_results.append((score1, score2))

        # Terminez le round et mettez à jour les scores
        current_round.end_round(match_results)
        print("Round terminé et scores mis à jour.")

        # Sauvegardez l'état du tournoi
        self.save_tournaments()

    def show_current_results(self, tournament):
        print("Résultats actuels du tournoi :")
        tournament.show_results()

        # Trier les joueurs par score
        sorted_players = sorted(
            tournament.players, key=lambda player: player.score, reverse=True
        )

        # Générer des paires à partir de la liste
        for i in range(0, len(sorted_players), 2):
            print(
                f"Paire: {sorted_players[i].first_name} {sorted_players[i].last_name} (Score: {sorted_players[i].score}) "
                f"vs {sorted_players[i+1].first_name} {sorted_players[i+1].last_name} (Score: {sorted_players[i+1].score})"
            )


@property
def get_matches_controller(self):
    return self.matches_controller
