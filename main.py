# Importation du contrôleur principal à partir du module controller_main
from controller.controller_main import Main_controller


# Crée une instance du contrôleur principal.
def main():
    main_controller = Main_controller()
    main_controller.run()


if __name__ == "__main__":
    main()
