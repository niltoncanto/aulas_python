import random
import time
import sys
#definindo duas variáveis globais
player_wins = 0
computer_wins = 0

def lancar_dado():
    tempo = 0.05
    giros = random.randint(5,20);
    for i in range(1, giros):
        numero = random.randint(1,6);
        print("\rnumero: ", numero, end="")
        print("\rO número sorteado foi: ", numero, end="")
        sys.stdout.flush()
        time.sleep(tempo)
        tempo += 0.05
    return numero

def dice():

    #gerar um número randomico
    #player = random.randint(1,6);
    print("Player jogando o dado...")
    player = lancar_dado()
    time.sleep(2)
    print("\n")
    print("Computador jogando o dado...")
    computer = lancar_dado()
    time.sleep(2)
    print("\n")
    if player > computer:
        print("Você ganhou!")
        global player_wins
        player_wins += 1
    elif player < computer:
        print("Você perdeu!")
        global computer_wins
        computer_wins += 1
    else:
        print("Empate!")
    print("\n")
    print("Você", player_wins, "x", computer_wins, "Computador")

while True:
    dice()
    print("Deseja jogar novamente? (s/n)")
    answer = input()
    if answer == 'n':
        break