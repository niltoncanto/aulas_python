import math

def primo(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        raiz_n = math.floor(math.sqrt(n))
        for i in range(2,raiz_n+1):
            if n % i == 0:
                return False
        return True
    
n = int(input("Digite um número inteiro: "))
print(primo(n))