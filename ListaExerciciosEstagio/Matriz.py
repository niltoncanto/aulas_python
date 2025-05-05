'''
Matriz: Dada uma matriz 2D de números, escreva uma função que calcule a soma dos elementos da diagonal principal. 
Comentário: você deve saber como acessar elementos em uma matriz 2D e como identificar a diagonal principal. 
Há váriações desse problema, por exemplo, com a diagonal secundária.
'''
def soma_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(soma_diagonal(matriz))