from datetime import datetime


class tournaments:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        rounds=4,
        players=None,
        description="",
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = 4
        self.current_round_number = 0
        self.rounds = []
        self.players = players if players is not None else []
        self.description = description

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def start_new_round(self):
        if self.current_round_number < self.number_of_rounds:
            new_round = rounds("Round " + str(self.current_round_number + 1))
            new_round = rounds
            self.rounds.append(new_round)
            self.current_round_number += 1
            new_round.start()
            return new_round
        else:
            raise ValueError("Nombre maximum de tours atteint.")


class rounds:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.matches = []

    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()

    def add_match(self, match):
        self.matches.append(match)
