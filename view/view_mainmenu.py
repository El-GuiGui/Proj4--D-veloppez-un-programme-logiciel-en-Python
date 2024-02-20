class main_menu_view:
    def show_menu(self):
        """
        Affiche le menu principal

        """
        print("\nMenu Principal")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Quitter")
        choix = input("Entrez le numéro de votre choix : ")
        return choix


class player_main_menu_view:
    def show_menu(self):
        """
        Affiche le menu de la gestion des joueurs

        """
        print("\nMenu de la Gestion des Joueurs")
        print("1. Ajouter un nouveau joueur")
        print("2. Mettre à jour un joueur existant")
        print("3. Supprimer un joueur")
        print("4. Afficher tous les joueurs")
        print("5. Afficher les joueurs par score")
        print("6. Afficher les joueurs par ordre alphabétique")
        print("7. Retourner au menu principal")
        print("8. Quitter")

        choix = input("Entrez le numéro de votre choix : ")
        return choix


class tournament_main_menu_view:
    def show_menu(self):
        """
        Affiche le menu de la gestion des tournois

        """
        print("\nMenu de la Gestion des Tournois")
        print("1. Créer un nouveau tournoi")
        print("2. Afficher les détails d'un tournoi")
        print("3. Lister tous les tournois")
        print("4. Reprendre un tournoi")
        print("5. Retourner au menu principal")
        choix = input("Entrez le numéro de votre choix : ")
        return choix

    def show_manage_tournament_menu(self):
        """
        Affiche le menu de la gestion d'un tournoi

        """
        print("\n--- Gestion du Tournoi ---")
        print("1. Inscrire des joueurs")
        print("2. Démarrer le prochain round")
        print("3. Afficher les résultats actuels")
        print("4. Générer les paires de joueurs")
        print("5. Retourner au menu des tournois")
        choix = input("Entrez le numéro de votre choix : ")
        return choix
