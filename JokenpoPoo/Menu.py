class Menu:
    @staticmethod
    def mostrar_menu():
        print("Bem-vindo ao jogo de Jokenpo!")
        print("Escolha: 'pedra', 'papel', 'tesoura' ou 'sair' para sair do jogo.")

    @staticmethod
    def perguntar_escolha():
        return input("Escolha sua jogada: ")