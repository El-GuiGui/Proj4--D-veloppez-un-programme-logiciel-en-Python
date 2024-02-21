from datetime import datetime


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    # Méthode pour sérialiser un match pour la sauvegarde JSON
    def serialize(self):
        return {
            "player1": self.player1.chess_id,  # Utilisez l'ID pour la sérialisation
            "player2": self.player2.chess_id,
            "score1": self.score1,
            "score2": self.score2,
        }


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    # Méthode pour sérialiser un round pour la sauvegarde JSON
    def serialize(self):
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": [match.serialize() for match in self.matches],
        }

    def end_round(self):
        self.end_time = datetime.now()


"""
    def set_winner(self, winner):
        self.winner = winner
        self.loser = self.player1 if winner == self.player2 else self.player2

    def get_winner(self):
        if self.scores[0] > self.scores[1]:
            return self.players[0]
        elif self.scores[0] < self.scores[1]:
            return self.players[1]
        else:
            # Match nul
            return None
"""
