from model.model_matchs import Round


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        players=[],
        rounds=None,
        description="",
        current_round=0,
        matches=[],
        number_of_rounds=4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.rounds = rounds if rounds is not None else []
        self.current_round = current_round
        self.matches = matches
        self.description = description
        self.number_of_rounds = number_of_rounds

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
            "current_round": self.current_round,
            "matches": self.matches,
            "description": self.description,
            "rounds": [round.serialize() for round in self.rounds],
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
        # Trier les joueurs par score
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
