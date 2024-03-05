from datetime import datetime


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def set_scores(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        # Met à jour les scores des joueurs
        self.player1.score += score1
        self.player2.score += score2

    # Méthode pour sérialiser un match
    def serialize(self):
        return {
            "player1": self.player1.chess_id,  # a verifier ........
            "player2": self.player2.chess_id,
            "score1": self.score1,
            "score2": self.score2,
        }


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matchs = []
        self.is_finished = False

    def add_match(self, match):
        self.matchs.append(match)

    def serialize(self):
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": [Match.serialize() for Match in self.matchs],
        }

    def end_round(self, match_results):
        """
        Termine le round et met à jour les scores des matches.

        """
        self.end_time = datetime.now()
        for match, (score1, score2) in zip(self.matchs, match_results):
            match.set_scores(score1, score2)
        self.is_finished = True
