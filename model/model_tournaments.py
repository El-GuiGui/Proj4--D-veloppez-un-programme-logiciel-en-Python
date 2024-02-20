from datetime import datetime


class Tournament:
    def __init__(
        self, name, location, start_date, end_date, players=[], rounds=4, description=""
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.current_round = 0
        self.matches = []
        self.description = description

    def add_player(self, player):
        """
        Ajoute un joueur au tournoi
        """
        if player not in self.players:
            self.players.append(player)

    def tournament_serialize(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "players": [player.players_serialize() for player in self.players],
            "rounds": self.rounds,
            "current_round": self.current_round,
            "matches": self.matches,
            "description": self.description,
        }

    def start_new_round(self):
        """
        Démarre un nouveau round (si le nombre actuel de rounds est inférieur à 4).
        """
        if len(self.rounds) < 4:
            round_name = f"Round {len(self.rounds) + 1}"
            new_round = Round(round_name)
            self.rounds.append(new_round)
            return new_round
        else:
            raise ValueError(
                "Le nombre maximum de rounds pour ce tournoi a été atteint."
            )

    def show_results(self):
        """a modifier"""
        pass


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matches = []

    def end_round(self):
        """
        Marque la fin du round.
        """
        self.end_time = datetime.now()


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.loser = None

    def set_winner(self, winner):
        """
        Définit le gagnant du match.
        """
        self.winner = winner
        self.loser = self.player1 if winner == self.player2 else self.player2
