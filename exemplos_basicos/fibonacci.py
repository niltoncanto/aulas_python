def fibonacci(n):
    if n <= 0:
        return []  # Retorna uma lista vazia para n não positivo
    elif n == 1:
        return [0]  # A sequência até o primeiro termo é [0]
    elif n == 2:
        return [0, 1]  # A sequência até o segundo termo é [0, 1]

    # Lista inicial da sequência com os dois primeiros termos
    fib_sequence = [0, 1]
    
    # Gera a sequência até o n-ésimo termo
    for i in range(2, n):
        # O próximo termo é a soma dos dois últimos termos da sequência
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence
    
try:
    n = int(input())
    if n>0 and n<46:
        r = fibonacci(n)
        t = ''
        for i in r:
            t += str(i) + " "
        t = t.strip()
        print(t)
            
except Error:
    print("Entrada inválida")