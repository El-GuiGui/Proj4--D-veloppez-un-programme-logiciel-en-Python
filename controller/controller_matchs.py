# Importation des modules nécessaires
from model.model_matchs import Match


class MatchsController:
    # Initialisation du contrôleur de matchs avec le contrôleur de tournois
    def __init__(self, tournaments_controller):
        self.tournaments_controller = tournaments_controller

    # Crée un match dans un tournoi et un round donnés, avec deux joueurs
    def create_match(self, tournament_name, round_name, player1, player2):
        tournament = self.tournaments_controller.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round:
                match = Match(player1, player2)
                round.matchs.append(match)
                self.tournaments_controller.save_tournaments()

    # Enregistre le résultat d'un match spécifique dans un tournoi et round donnés
    def record_match_result(self, tournament_name, round_name, match_index, score1, score2):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round and len(round.matchs) > match_index:
                match = round.matchs[match_index]
                match.set_scores(score1, score2)
                self.tournaments_controller.save_tournaments()

    # Termine un round spécifique dans un tournoi donné
    def end_round(self, tournament_name, round_name):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round:
                round.end_round()
                self.tournaments_controller.save_tournaments()

    # Trouve un tournoi par son nom dans la liste des tournois
    def find_tournament_by_name(self, tournament_name):
        for tournament in self.tournaments_controller.tournaments:
            if tournament.name == tournament_name:
                return tournament
        return None

    # Trouve un round par son nom dans un tournoi spécifié
    def find_round_by_name(self, tournament, round_name):
        for round in tournament.rounds:
            if round.name == round_name:
                return round
        return None
