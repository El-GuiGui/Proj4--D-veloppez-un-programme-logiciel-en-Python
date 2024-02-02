class players:
    def __init__(self, first_name, last_name, birth_date, chess_id, rank=None, score=0):
        # Identifiant national d'échecs
        self.chess_id = chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.rank = rank
        self.score = score


def update_score(self, points):
    # Met à jour le score suivant les points gagnés
    self.score += points


def compare_score(self, other_player):
    # Compare le score entre ce joueur et un autre, Renvoie True si ce joueur a un score plus élevé à l'autre, sinon False.
    return self.score > other_player.score


def __str__(self):
    # Retourne les informations du joueur.
    return f"{self.first_name} {self.last_name} {self.birth_date} (ID: {self.chess_id}), Score: {self.score}, Rank: {self.rank}"


# db ? link ?
