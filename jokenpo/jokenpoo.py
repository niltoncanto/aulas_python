import random

# Lista das possíveis escolhas no jogo
escolhas = ["papel","tesoura","pedra"]

# Variáveis para armazenar as escolhas e os resultados
jogador = ''
computador = ''
vitorias_jog = 0
vitorias_comp = 0
empates = 0

# Laço principal do jogo
while True:
    try: # Início do bloco try
        print("\n*********** Jokenpo ***********")
        print("Opções: ")
        print("Digite sua opção: ")
        print("papel")
        print("tesoura")
        print("pedra")
        jogador = input("Sua escolha: ").lower() # Recebe a escolha do jogador e converte para minúsculas

        if jogador not in escolhas:
            print("Opção inválida!\n")
            continue

        computador = random.choice(escolhas)

        if jogador == computador:
            empates += 1
            print("Empatou!\n")
        elif ((jogador == "tesoura" and computador == "papel") or 
              (jogador == "pedra" and computador == "tesoura") or 
              (jogador == "papel" and computador == "pedra")):
            vitorias_jog += 1
            print("Você ganhou!")
        else:
            vitorias_comp += 1
            print("Computador ganhou!\n")

        print("*******************************")
        print("           PLACAR              ")
        print("computador => " + str(vitorias_comp))
        print("Jogador => " + str(vitorias_jog))
        print("Empates => " + str(empates))
        print("*******************************\n")
        resposta = input("Deseja continuar s/n : ")

        if resposta.lower() in ['n', 'não', 'nao']:
            break
    except Exception as e: # Caso ocorra uma exceção, este bloco irá lidar com ela
        print(f"Ocorreu um erro: {e}")
        print("Por favor, tente novamente.\n")
        continue  # Continua com a próxima iteração do laço

print("Obrigado por jogar! Até mais!")
