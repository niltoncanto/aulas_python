import random
escolhas = ["papel","tesoura","pedra"]
jogador = ''
computador = ''
vitorias_jog =0
vitorias_comp =0
empates =0

while True:
    print("Digite sua opção: ")
    print("papel")
    print("tesoura")
    print("pedra")
    jogador = input("Sua escolha: ")
    computador = random.choice(escolhas)
    print(jogador,computador)
    if(jogador==computador):
        empates += 1
        print("empatou")
    elif((jogador=="tesoura" and computador=="papel") or \
        (jogador=="pedra" and computador=="tesoura") or \
        (jogador=="papel" and computador=="pedra")):
        vitorias_jog +=1
        print("Você ganhou!")
    else:
        vitorias_comp +=1
        print("Computador ganhou!")
    print("computador => " + str(vitorias_comp))
    print("Jogador => " + str(vitorias_jog))
    print("Empates => " + str(empates))
    resposta = input("Deseja continuar s/n : ")
    if(resposta.lower()=='n' or resposta.lower=="não" or resposta.lower=="nao"):
        break







