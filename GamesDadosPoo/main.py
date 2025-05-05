class Main:
    @staticmethod
    def executar_programa():
        jogo = JogoDeDados()
        Menu.mostrar_menu()
        resposta = input()
        while resposta == 's':
            jogo.jogar_rodada()
            resposta = Menu.perguntar_jogar_novamente()
        print("Obrigado por jogar!")

if __name__ == "__main__":
    Main.executar_programa()
