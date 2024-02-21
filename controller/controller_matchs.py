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
                round.matches.append(match)
                self.tournaments_controller.save_tournaments()

    def record_match_result(
        self, tournament_name, round_name, match_index, score1, score2
    ):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round and len(round.matches) > match_index:
                match = round.matches[match_index]
                match.score1 = score1
                match.score2 = score2
                self.save_tournaments()

    def end_round(self, tournament_name, round_name):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            round = self.find_round_by_name(tournament, round_name)
            if round:
                round.end_round()
                self.save_tournaments()
