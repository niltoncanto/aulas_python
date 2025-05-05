# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. 
# Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. 
# A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. 
# Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.
import math
def primo(n):
    if n<=3:
        return f"{n} eh primo"
    if n%2==0:
        return f"{n} nao eh primo"
    else:
        raiz_n = math.sqrt(n)
        #print(n,math.ceil(raiz_n),raiz_n,list(range(1,math.ceil(raiz_n)+1)))
        for i in range(2,math.ceil(raiz_n)+1):
            if n % i == 0:
                return f"{n} nao eh primo"
                
        return f"{n} eh primo"

try:
    n_testes = int(input())
    if n_testes<=100:
        for i in range(0,n_testes):
            try:
                n = int(input())
                if n<10**7:
                    print(primo(n))
                else:
                    print("entrada inválida")
            except ValueError:
                print("Entrada inválida")
    else:
        print("Número de Testes inválido.")
except ValueError:
        print("Entrada inválida")
