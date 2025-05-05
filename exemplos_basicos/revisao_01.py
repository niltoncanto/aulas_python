#jokenpo
import random
jogador = ''
computador = ''
empates = 0
v_jogador = 0
v_computador = 0
opcoes = ['pedra','tesoura','papel']

def menu():
    global jogador
    while True:
        print("****** Menu ******")
        print("Pedra")
        print("Papel")
        print("Tesoura")
        jogador = input("Entre com sua opção: ")
        jogador = jogador.lower()
        if jogador not in opcoes:
            print("Opção inválida, tente novamente")
            continue
        print(f"\nJogador:{jogador}")
        jokenpo()

def placar():
    global v_jogador,v_computador,empates
    print("****** Placar ******")
    print(f"Jogador: {v_jogador}")
    print(f"Computador: {v_computador}")
    print(f"Empates: {empates}")
    print("********************")
    res = input("Deseja continuar (s/n): ")
    res.lower()
    if res!='s' or res!='sim':
        exit()
    else:
        menu()

def jokenpo():
    global computador,empates,v_jogador,v_computador
    computador = random.choice(opcoes)
    print(f"Computador:{computador}\n")
    if jogador == computador:
        empates +=1
    elif jogador=='pedra' and computador == 'tesoura':
        v_jogador +=1
    elif jogador=='tesoura' and computador == 'papel':
        v_jogador +=1
    elif jogador=='papel' and computador == 'pedra':
        v_jogador +=1
    else:
        v_computador +=1
    placar()

menu()
    

