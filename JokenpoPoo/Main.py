from Jokenpo import Jokenpo
from Menu import Menu

class Main:
    @staticmethod
    def executar_programa():
        jogo = Jokenpo()
        while True:
            Menu.mostrar_menu()
            escolha = Menu.perguntar_escolha()
            if escolha.lower() == 'sair':
                print("Obrigado por jogar!")
                break
            if escolha.lower() not in jogo.choices:
                print("Escolha inválida! Tente novamente.")
                continue
            jogo.jogar_rodada(escolha.lower())

if __name__ == "__main__":
    Main.executar_programa()
