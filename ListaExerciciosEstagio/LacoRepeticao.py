'''
Laço de repetição: Escreva um loop que imprima os números de 1 a 100, mas para múltiplos de 3 imprima "Fizz", 
para múltiplos de 5 imprima "Buzz" e para múltiplos de ambos imprima "FizzBuzz". 
Comentário: é uma questão clássica que testa a lógica básica e o controle de fluxo.
'''
def long_string(lista):
    maior = 0
    string = ""
    for i in lista:
        if len(i) > maior:
            maior = len(i)
            string = i
    return maior,string

lista = ["FizzBuzz", "Fizz FizzBuzz FizzBuzz", "Buzz Buzz", "FizzBuzz FizzBuzz FizzBuzz"]
print(long_string(lista))