def print_matriz(matriz):
    # Função para imprimir uma matriz formatada com espaçamento entre os elementos
    N = len(matriz)
    # Determina o tamanho da matriz (número de linhas/colunas, já que é uma matriz quadrada)
    for i in range(N):
        # Itera sobre as linhas da matriz
        for j in range(N):
            # Itera sobre as colunas de cada linha
            if j == N - 1:
                # Se for o último elemento da linha, imprime sem adicionar um espaço depois
                print(f'{matriz[i][j]:3}', end='')
                # Imprime o elemento da matriz formatado com 3 espaços de largura
            else:
                print(f'{matriz[i][j]:3}', end=' ')
                # Para os demais elementos, imprime o número seguido de um espaço
        print()  # Imprime uma nova linha após terminar cada linha da matriz
    print()  # Imprime uma linha em branco após a impressão da matriz completa
while True:
    # Loop infinito para repetidamente ler entradas e processar matrizes
    N = int(input())
    # Lê o tamanho da matriz (N x N) da entrada
    if N == 0:
        break
        # Se o valor de N for 0, encerra o loop e termina o programa
    matriz = [[0] * N for _ in range(N)]
    # Inicializa uma matriz N x N preenchida com zeros
    camada = 1
    # Variável para controlar o preenchimento de camadas concêntricas com números crescentes
    for k in range((N + 1) // 2):
        # Loop para controlar as camadas concêntricas de números. Divide N por 2 (arredondado para cima)
        # pois o padrão de preenchimento começa do exterior e vai até o centro da matriz.
        for i in range(k, N - k):
            # Preenche as linhas da matriz da linha k até a linha N-k-1 (excluindo as bordas externas já preenchidas)
            for j in range(k, N - k):
                # Preenche as colunas da matriz da coluna k até a coluna N-k-1 (excluindo as bordas externas já preenchidas)
                matriz[i][j] = camada
                # Preenche a posição [i][j] da matriz com o valor atual da camada
        camada += 1
        # Após preencher uma camada, aumenta o valor da camada para o próximo número
    print_matriz(matriz)
    # Chama a função print_matriz para imprimir a matriz preenchida
