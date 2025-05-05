import random
import time
import sys

class JogoDeDados:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def lancar_dado(self):
        tempo = 0.05
        giros = random.randint(5,20)
        for i in range(1, giros):
            numero = random.randint(1,6)
            print("\rO número sorteado foi: ", numero, end="")
            sys.stdout.flush()
            time.sleep(tempo)
            tempo += 0.05
        return numero

    def jogar_rodada(self):
        print("Player jogando o dado...")
        player = self.lancar_dado()
        time.sleep(2)
        print("\n")
        print("Computador jogando o dado...")
        computer = self.lancar_dado()
        time.sleep(2)
        print("\n")
        if player > computer:
            print("Você ganhou!")
            self.player_wins += 1
        elif player < computer:
            print("Você perdeu!")
            self.computer_wins += 1
        else:
            print("Empate!")
        print("\n")
        print("Você", self.player_wins, "x", self.computer_wins, "Computador")
