'''
Escreva uma função que retorne o n-ésimo número da sequência Fibonacci. Comentário: você pode usar uma abordagem recursiva ou iterativa. 
A solução recursiva simples tem uma performance ruim, mas pode ser otimizada com memoização.
Fn = Fn - 1 + Fn - 2
Assim, começando pelo 1, essa sequência é formada somando cada numeral com o numeral que o antecede. No caso do 1, repete-se esse numeral e soma-se, ou seja, 1 + 1 = 2.
De seguida soma-se o resultado com o numeral que o antecede, ou seja, 2 + 1 = 3 e assim sucessivamente, numa sequência infinita:
3 + 2 = 5
5 + 3 = 8
8 + 5 = 13
13 + 8 = 21
21 + 13 = 34
34 + 21 = 55
55 + 34 = 89
'''
def fibonacci_recursiva(n):
    if n <= 2:
        return n
    else:
        return fibonacci_recursiva(n-1) + fibonacci_recursiva(n-2) 

def fibonacci_iterativa(n):
    a,b = 0,1
    for k in range(n):
            s = a+b
            a = b
            b= s
    return b

n = int(input("Digite um número inteirox: "))
print("recursiva")
for i in range(1, n+1):
    print(i,fibonacci_recursiva(i))
print("interativa")
for i in range(1, n+1):
     print(i,fibonacci_iterativa(i))

