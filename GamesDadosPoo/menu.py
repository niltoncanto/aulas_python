class Menu:
    @staticmethod
    def mostrar_menu():
        print("Bem-vindo ao jogo de lançar dados!")
        print("Digite 's' para começar ou 'n' para sair.")

    @staticmethod
    def perguntar_jogar_novamente():
        print("Deseja jogar novamente? (s/n)")
        return input()
