def entrada_dados():
    m = int(input())
    estrutura = []
    for j in range(m):
        a, b = map(int, input().split())
        estrutura.append((a, b))
    return estrutura

def testa_pilha(pilha):
    stack = []
    for comando, valor in pilha:
        if comando == 1:  # Empilhar
            stack.append(valor)
        elif comando == 2:  # Desempilhar
            if not stack or stack.pop() != valor:
                return False
    return True
    
def testa_fila(fila):
    queue = []
    for comando, valor in fila:
        if comando == 1:  # Enfileirar
            queue.append(valor)
        elif comando == 2:  # Desenfileirar
            if not queue or queue.pop(0) != valor:
                return False
    return True

def testa_fila_prioridade(fila_prioridade):
    heap = []
    for comando, valor in fila_prioridade:
        if comando == 1:  # Inserir na fila de prioridade
            heap.append(valor)
        elif comando == 2:  # Remover o maior valor
            if not heap or max(heap) != valor:
                return False
            heap.remove(max(heap))
    return True

#import heapq

'''def testa_fila_prioridade(fila_prioridade):
    heap = []
    for comando, valor in fila_prioridade:
        if comando == 1:  # Inserir na fila de prioridade
            heapq.heappush(heap, -valor)  # Negativo para simular uma max-heap
        elif comando == 2:  # Remover o maior valor
            if not heap or -heapq.heappop(heap) != valor:
                return False
    return True'''

if __name__=="__main__":
    while True:
        try:
            estrutura = entrada_dados()
            eh_pilha = testa_pilha(estrutura)
            eh_fila = testa_fila(estrutura)
            eh_fila_prioridade = testa_fila_prioridade(estrutura)

            if eh_pilha + eh_fila + eh_fila_prioridade > 1:
                print("not sure")
            elif eh_pilha:
                print("stack")
            elif eh_fila:
                print("queue")
            elif eh_fila_prioridade:
                print("priority queue")
            else:
                print("impossible")
        except Exception:
            break