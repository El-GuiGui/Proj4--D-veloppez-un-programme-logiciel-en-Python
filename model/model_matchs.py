class matchs:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        # Initialiser scores à 0
        self.scores = [0, 0]

    def set_result(self, result):
        # result (score1, score2)
        self.scores = result

    def get_winner(self):
        if self.scores[0] > self.scores[1]:
            return self.players[0]
        elif self.scores[0] < self.scores[1]:
            return self.players[1]
        else:
            # Match nul
            return None
