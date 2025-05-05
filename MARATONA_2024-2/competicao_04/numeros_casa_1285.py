while True:
    try:
        inicio,fim = map(int,input().split())
        numeros = 0
        for a in range(inicio,fim+1):
            a = str(a) #transforma em string
            b = set(a) #transforma em conjunto
            if len(a)==len(b):
                numeros+=1
        print(numeros)
    except EOFError:
        break
