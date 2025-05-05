def busca_binaria(arr,item):
    inicio = 0
    fim = len(arr)-1
    while inicio<=fim:
        indice_meio = (inicio + fim) // 2
        valor_meio = arr[indice_meio]
        if valor_meio == item:
            return indice_meio 
        
        if item<=valor_meio:
            fim = indice_meio - 1
        else:
            inicio = indice_meio + 1

    return None

#exemplo de aplicação
arr = [1, 2, 3, 4, 5, 6, 7, 8]
item = 6
resp = busca_binaria(arr,item)
print(resp) #deve retornar 5
item = 9
resp = busca_binaria(arr,item)
print(resp) # deve retornar None

'''
[1, 2, 3, 4, 5]
[7, 8]
[6] 
'''
