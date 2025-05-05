from random import randint
print("jdadv")
comp = randint(0,100)
contador = 0
while True:
    print("Entre com um número inteiro entre 0 e 100")
    jog = int(input())
    contador+=1
    if jog == comp:
        print("ganhou")
        print(f"número de tentativas:{contador}")
        break
    elif jog > comp:
        print(f"o número oculto é menor que {jog}")
    else:
        print(f"o número oculto é maior que {jog}")

