import random  # Importa o módulo 'random' para gerar escolhas aleatórias
# Lista das possíveis escolhas no jogo
escolhas = ["papel","tesoura","pedra"]
# Variáveis para armazenar a escolha do jogador e do computador
jogador = ''
computador = ''
# Variáveis para armazenar o número de vitórias e empates
vitorias_jog = 0
vitorias_comp = 0
empates = 0
# Laço principal do jogo
while True:
    print("\n")
    print("*********** Jokenpo ***********")
    print("Opções: ")
    print("Digite sua opção: ")  # Solicita ao jogador para escolher uma opção
    print("papel")
    print("tesoura")
    print("pedra")
    jogador = input("Sua escolha: ")  # Lê a escolha do jogador
    
    #print("\n")
    jogador = jogador.lower()  # Converte a escolha do jogador para minúsculas
    # Verifica se a escolha do jogador é válida
    if jogador not in escolhas:
        print("Opção inválida!\n")
        continue  # Se inválida, volta ao início do laço
    computador = random.choice(escolhas)  # Escolha aleatória do computador
    print(f"Computador: {computador}")
    # Verifica o resultado do jogo
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
    # Imprime o placar
    print("*******************************")
    print("           PLACAR              ")
    print("computador => " + str(vitorias_comp))
    print("Jogador => " + str(vitorias_jog))
    print("Empates => " + str(empates))
    print("*******************************")
    print("\n")
    resposta = input("Deseja continuar s/n : ")  # Pergunta se o jogador quer continuar
    
    # Verifica se o jogador deseja sair do jogo
    if resposta.lower() == 'n' or resposta.lower() == "não" or resposta.lower() == "nao":
        break  # Se o jogador desejar sair, encerra o laço
