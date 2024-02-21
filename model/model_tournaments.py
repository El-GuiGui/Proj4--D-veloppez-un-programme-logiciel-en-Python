from datetime import datetime


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        players=[],
        rounds=4,
        description="",
        current_round=0,
        matches=[],
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds
        self.current_round = current_round
        self.matches = matches
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

    def start_new_round(self, name):
        if self.current_round < self.rounds:
            new_round = Round(name)
            self.current_round += 1
            self.rounds.append(new_round)
            return new_round
        else:
            raise ValueError("Nombre maximum de rounds atteint.")

    def show_results(self):
        # Vérifie si aucun round n'a été commencé
        if self.current_round == 0:
            print("Aucun round n'a été commencé. Veuillez commencer un round.")
            return

        print("\nClassement actuel des joueurs :")
        # Trier les joueurs par score décroissant
        sorted_players = sorted(self.players, key=lambda p: p["score"], reverse=True)
        for player in sorted_players:
            print(
                f"{player['first_name']} {player['last_name']} : {player['score']} points"
            )

        print("\nMatchs joués :")
        for round in self.rounds:
            print(f"{round.name}:")
            for match in round.matches:
                print(
                    f"  {match.player1['first_name']} vs {match.player2['first_name']} - Vainqueur : {'Match nul' if match.winner is None else match.winner['first_name']}"
                )


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
