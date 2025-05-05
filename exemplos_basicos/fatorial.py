def fatorial(n):
    """Calcula o fatorial de n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def encontrar_menor_k(N):
    """Encontra o menor número k para a soma de fatoriais."""
    k = 0  # Inicializa o contador de termos
    ai = []  # Lista para armazenar os termos da soma

    # Encontrar o maior fatorial menor ou igual a N
    soma = 0
    diferenca = N
    i = 0
    while diferenca>0:
        i +=1
        fat = fatorial(i)
        print(diferenca,fat,i)
        if fat>diferenca:
            diferenca -= fatorial(i-1)
            print(fat)
            k +=1
            i = 0
            continue
    return k   # Retorna o menor k e a lista de termos

# Exemplo de uso da função
N = 25
k = encontrar_menor_k(N)
print(k)  # Retorna o menor k e os termos da soma