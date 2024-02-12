class matchs:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        # Initialiser scores à 0
        self.scores = [0, 0]

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
