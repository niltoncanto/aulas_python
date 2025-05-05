import random

class Jokenpo:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.choices = ['pedra', 'papel', 'tesoura']

    def jogar_rodada(self, player_choice):
        computer_choice = random.choice(self.choices)
        print(f"Jogador escolheu: {player_choice}")
        print(f"Computador escolheu: {computer_choice}")
        
        if player_choice == computer_choice:
            print("Empate!")
        elif (player_choice == 'pedra' and computer_choice == 'tesoura') or \
             (player_choice == 'papel' and computer_choice == 'pedra') or \
             (player_choice == 'tesoura' and computer_choice == 'papel'):
            print("Você ganhou!")
            self.player_wins += 1
        else:
            print("Você perdeu!")
            self.computer_wins += 1
            
        print("\n")
        print("Você", self.player_wins, "x", self.computer_wins, "Computador")
