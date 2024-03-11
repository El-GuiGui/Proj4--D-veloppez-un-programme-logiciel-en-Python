# Importation des modules nécessaires
from model.model_matchs import Round


class Tournament:
    # Initialisation du tournoi
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

    # Ajoute un joueur à la liste des joueurs s'il n'y est pas déjà.
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    # Prépare les données du tournoi pour la sérialisation
    def tournament_serialize(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "players": [player.players_serialize() for player in self.players],
            "current_round": self.current_round,
            "description": self.description,
            "rounds": [round.serialize() for round in self.rounds],
        }

    # Commence un nouveau round si le nombre maximum de rounds n'a pas été atteint.
    def start_new_round(self, name):
        if self.current_round < self.rounds:
            new_round = Round(name)
            self.current_round += 1
            self.rounds.append(new_round)
            return new_round
        else:
            raise ValueError("Nombre maximum de rounds atteint.")

    # Affiche les résultats actuels du tournoi.
    def show_results(self):
        if self.current_round == 0:
            print("Aucun round n'a été commencé. Veuillez commencer un round.")
            return

        print("\nClassement actuel des joueurs :")
        # Trie les joueurs par score
        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)
        for player in sorted_players:
            print(f"{player.first_name} {player.last_name} : {player.score} points")

        print("\nMatchs joués :")
        for round in self.rounds:
            print(f"{round.name}:")
            for match in round.matchs:
                print(
                    f"  {match.player1.first_name} {match.player1.last_name}"
                    f" vs {match.player2.first_name} {match.player2.last_name}"
                )
