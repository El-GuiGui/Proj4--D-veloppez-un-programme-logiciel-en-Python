class players:
    # Initialisation des attributs du joueur
    def __init__(self, first_name, last_name, birth_date, chess_id, score=0):
        self.chess_id = chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.score = score

    # Convertit l'instance du joueur en un dictionnaire pour la sérialisation,
    def players_serialize(self):
        return {
            "chess_id": self.chess_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "score": self.score,
        }

    @classmethod
    # Crée une instance de la classe à partir du dictionnaire.
    def players_deserialize(cls, data):
        return cls(**data)


# Met à jour le score suivant les points gagnés
def update_score(self, points):
    self.score += points


# Compare le score entre deux joueurs
def compare_score(self, other_player):
    return self.score > other_player.score


# Retourne les informations du joueur.
def __str__(self):
    return f"{self.first_name} {self.last_name} {self.birth_date} (ID: {self.chess_id}), Score: {self.score}"
