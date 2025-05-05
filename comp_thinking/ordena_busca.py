def bubble_sort(lista):
    n = len(lista)
    for j in range(n):
        troca = False
        for i in range(0,n-j-1):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i] #atribuição multipla
                troca = True
        if troca is False:
            break
    return lista

#exemplo de uso
lista = [80, 10, 5, 4, 30, 33, 22, 21, 15] # 9 itens
bubble_sort(lista)
print(f"lista Ordenada: {lista}")



#######################################
def busca_binaria(lista,item):
    inicio = 0
    fim = len(lista) - 1
    while inicio<=fim:
        indice_meio = (inicio + fim) // 2
        valor_meio = lista[indice_meio]
        if valor_meio == item:
            return indice_meio
        
        if valor_meio>item:
            fim = indice_meio - 1
        else:
            inicio = indice_meio + 1

#exemplo de uso
#lista = [4, 5, 10, 15, 21, 22, 30, 33, 80]
item = 5
resp = busca_binaria(lista,5) # retorna posição 1 (o item com valor 15 está na posição 1 da lista)
resp = busca_binaria(lista,27) # retorna None (item não encontrado na lista)

'''
item = 5
inicio = 0
fim = 8
[4, 5, 10, 15, 21, 22, 30, 33, 80]
inicio = 0
fim = 3
[4, 5, 10, 15]
inicio = 0
fim = 1
[4, 5]
inicio = 0
fim = 0
[4]

'''