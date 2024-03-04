from model.model_matchs import Match, Round
from model.model_tournaments import Tournament


class MatchsController:
    def __init__(self, tournaments_controller):
        self.tournaments_controller = tournaments_controller

    def create_match(self, tournament_name, round_name, player1, player2):
        tournament = self.tournaments_controller.find_tournament_by_name(
            tournament_name
        )
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round:
                match = Match(player1, player2)
                round.matchs.append(match)
                self.tournaments_controller.save_tournaments()

    def record_match_result(
        self, tournament_name, round_name, match_index, score1, score2
    ):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round and len(round.matchs) > match_index:
                match = round.matchs[match_index]
                match.set_scores(score1, score2)
                self.tournaments_controller.save_tournaments()

    def end_round(self, tournament_name, round_name):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round:
                round.end_round()
                self.tournaments_controller.save_tournaments()

    def find_tournament_by_name(self, tournament_name):
        # Recherche un tournoi par nom
        for tournament in self.tournaments_controller.tournaments:
            if tournament.name == tournament_name:
                return tournament
        return None

    def find_round_by_name(self, tournament, round_name):
        # Recherche un round par nom dans un tournoi spécifié
        for round in tournament.rounds:
            if round.name == round_name:
                return round
        return None
