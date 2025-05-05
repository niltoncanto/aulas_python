def bubble_sort(arr): #função que recebe um array e retorna o array ordenado
    n = len(arr)
    for j in range(n):
        troca = False
        for i in range(0,n-j-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                troca = True
        if troca is not True:
            break
    return arr

#Exemplo de uso
arr = [6,5,3,1,8,7,2,4]
bubble_sort(arr)
print(f"Lista ordenada:{arr}")