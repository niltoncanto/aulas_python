import random

def jokenpo():
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    
    while True:
        print("\nEscolha entre Pedra, Papel e Tesoura.")
        jogador = input("Sua escolha: ")
        
        if jogador not in escolhas:
            print("Escolha inválida. Por favor, tente novamente.")
            continue

        computador = random.choice(escolhas)
        print("O computador escolheu:", computador)

        if jogador == computador:
            print("Empate!")
        elif (jogador == 'Pedra' and computador == 'Tesoura') or \
             (jogador == 'Tesoura' and computador == 'Papel') or \
             (jogador == 'Papel' and computador == 'Pedra'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            break

jokenpo()
