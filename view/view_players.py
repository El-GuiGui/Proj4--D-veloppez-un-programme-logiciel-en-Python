class Player_View:
    def get_player_details(self):
        """
        Informations nécessaires à la création d'un nouveau joueur
        """
        print("Entrer les détails du joueur :")
        first_name = input("Prénom : ")
        last_name = input("Nom de famille : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        chess_id = input("Identifiant d'échecs : ")
        rank = None
        score = 0

        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "chess_id": chess_id,
            "rank": rank,
            "score": score,
        }

    def update_player_details(self, player):
        """
        Met à jour les détails d'un joueur existant
        """
        print(
            f"Mise à jour des informations pour {player.first_name} {player.last_name}:"
        )
        player.first_name = (
            input(f"Nouveau prénom ({player.first_name}): ") or player.first_name
        )
        player.last_name = (
            input(f"Nouveau nom de famille ({player.last_name}): ") or player.last_name
        )
        player.birth_date = (
            input(f"Nouvelle date de naissance ({player.birth_date}): ")
            or player.birth_date
        )
        player.chess_id = (
            input(f"Nouvel identifiant d'échecs ({player.chess_id}): ")
            or player.chess_id
        )
        return player

    def show_player_details(self, player):
        """
        Affiche les détails d'un joueur
        """
        print("\n------------------- Détails du Joueur -------------------")
        print(f"Nom : {player.last_name}, Prénom : {player.first_name}")
        print(f"Date de naissance : {player.birth_date}")
        print(f"Identifiant d'échecs : {player.chess_id}")
        print(
            f"Classement : {player.rank if player.rank is not None else 'Non classé'}"
        )
        print(f"Score : {player.score}")
        print("--------------------------------------------------------")

    def show_players_list(self, players):  # view -> controller player show
        """
        Affiche une liste de tous les joueurs.
        """
        for player in players:
            self.show_player_details(player)

    def show_players_by_score(self, players):
        """
        Affiche les joueurs triés par score.
        """
        sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
        self.show_players_list(sorted_players)

    def show_players_alphabetically(self, players):
        """
        Affiche les joueurs triés par ordre alphabétique (nom)
        """
        sorted_players = sorted(players, key=lambda x: x.last_name)
        self.show_players_list(sorted_players)
