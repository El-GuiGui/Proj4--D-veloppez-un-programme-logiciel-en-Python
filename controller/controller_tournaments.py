# from model.model_tournaments import tournaments

from view.view_mainmenu import tournament_main_menu_view


class Tournament_Controller:
    def __init__(self):
        self.tournaments = []
        self.view = tournament_main_menu_view()

    def viewchoice(self):
        while True:
            choix = self.view.show_menu()
            if choix == "1":
                self.create_tournament()
            elif choix == "2":
                self.show_tournament_details()
            elif choix == "3":
                self.list_tournaments()
            elif choix == "4":
                self.resume_tournaments
            elif choix == "5":
                break
            else:
                print("Choix non valide, réessayer !")

    def manage_tournament(self, tournament):
        while True:
            choix = self.view.show_manage_tournament_menu()
            if choix == "1":
                self.register_players(tournament)
            elif choix == "2":
                self.start_next_round(tournament)
            elif choix == "3":
                self.show_current_results(tournament)
            elif choix == "4":
                self.generate_player_pairs(tournament)
            elif choix == "5":
                break  # Retour au menu des tournois
            else:
                print("Choix non valide, réessayer !")

    def show_tournament_details(self):
        tournament_name = input("Entrez le nom du tournoi : ")
        found = False
        for tournament in self.tournaments:
            if tournament.name.lower() == tournament_name.lower():
                self.view.show_tournament_details(tournament)
                found = True
                break
        if not found:
            print("Tournoi non trouvé.")

    def list_tournaments(self):
        if not self.tournaments:
            print("Aucun tournoi disponible.")
        else:
            for tournament in self.tournaments:
                print(
                    f"Nom : {tournament.name}, Lieu : {tournament.location}, Dates : {tournament.start_date} à {tournament.end_date}"
                )

    def create_tournament(self):
        details = self.view.show_manage_tournament_menu()
        new_tournament = Tournament(*details)
        self.tournaments.append(new_tournament)
        print("Tournoi créé avec succès. Passons à la gestion du tournoi.")
        self.manage_tournament(new_tournament)
