def criar_matriz_padrao(n):
    # Função para criar uma matriz de tamanho n x n, seguindo um padrão específico de preenchimento
    # n: dimensão da matriz (número de linhas e colunas)
    matriz = [[3 for _ in range(n)] for _ in range(n)]
    # Inicializa uma matriz n x n onde todos os elementos são 3
    # [[3, 3, 3, ..., 3], ..., [3, 3, 3, ..., 3]]
    pos1, pos2 = 0, n-1
    # Define as posições iniciais para inserir o número 1 (na coluna à esquerda) e o número 2 (na coluna à direita)
    # pos1 começa na primeira coluna (0) e pos2 começa na última coluna (n-1)
    for i in range(n):
        # Itera sobre as linhas da matriz (de 0 até n-1)
        matriz[i][pos1] = 1
        # Na linha i, coloca o número 1 na coluna correspondente à variável pos1
        # Inicialmente, isso coloca o número 1 na diagonal principal, depois vai movendo para a direita
        matriz[i][pos2] = 2
        # Na linha i, coloca o número 2 na coluna correspondente à variável pos2
        # Inicialmente, isso coloca o número 2 na diagonal secundária, depois vai movendo para a esquerda
        pos1 = (pos1 + 1)
        # Atualiza a posição de pos1 para a próxima linha, movendo uma coluna à direita
        pos2 = (pos2 - 1)
        # Atualiza a posição de pos2 para a próxima linha, movendo uma coluna à esquerda
    return matriz
    # Retorna a matriz preenchida de acordo com o padrão
def imprimir_matriz(matriz):
    # Função para imprimir a matriz formatada em linhas contínuas
    # matriz: lista de listas representando a matriz a ser impressa
    for linha in matriz:
        # Itera sobre cada linha da matriz
        print(''.join(map(str, linha)))
        # Converte cada elemento da linha para string e os une sem espaços entre eles, em seguida imprime a linha
entradas = []
# Inicializa uma lista vazia para armazenar os valores de entrada (tamanhos da matriz)
while True:
    # Loop infinito que tenta ler entradas do usuário até que o fim do arquivo seja alcançado (EOF)
    try:
        entrada = input()
        # Tenta ler uma nova linha de entrada do usuário (número que define o tamanho da matriz)
        n = int(entrada)
        # Converte a entrada para um número inteiro (o valor de n para criar a matriz)
        entradas.append(n)
        # Adiciona o valor de n à lista de entradas
    except EOFError:
        # Quando o fim do arquivo (EOF) é alcançado, o código gera uma exceção (EOFError)
        break
        # Sai do loop quando não houver mais entradas
for i in entradas:
    # Itera sobre os valores de n na lista de entradas
    matriz = criar_matriz_padrao(i)
    # Chama a função criar_matriz_padrao para gerar uma matriz com o tamanho n
    imprimir_matriz(matriz)
    # Chama a função imprimir_matriz para exibir a matriz no formato desejado
