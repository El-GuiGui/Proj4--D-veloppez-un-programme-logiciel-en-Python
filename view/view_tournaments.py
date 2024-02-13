class tournaments_view:
    def get_tournament_details(self):
        """Demande et retourne les détails pour la création d'un nouveau tournoi."""
        print("\n--- Création d'un nouveau tournoi ---")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (JJ/MM/AAAA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        description = input("Description (facultatif) : ")
        return name, location, start_date, end_date, description

    def show_tournament_details(self, tournament):
        """Affiche les détails d'un tournoi spécifique."""
        print(f"\n--- Détails du Tournoi : {tournament.name} ---")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.start_date}")
        print(f"Date de fin : {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de joueurs inscrits : {len(tournament.players)}")
