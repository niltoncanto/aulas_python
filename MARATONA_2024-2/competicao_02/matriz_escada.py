def verificar_matriz_escada(n, m, matriz):
    # Função que verifica se a matriz dada está na forma de "matriz escalonada"
    # n: número de linhas da matriz
    # m: número de colunas da matriz
    # matriz: matriz bidimensional a ser verificada
    indice_coluna_anterior = -1
    # Variável que armazena o índice da coluna do último elemento não zero encontrado em uma linha anterior.
    # Inicializa com -1 para indicar que não foi encontrado nenhum elemento não zero até o momento.
    for i in range(n):
        # Loop através das linhas da matriz (de 0 até n-1)
        encontrou_nao_zero = False
        # Variável de controle para verificar se há um elemento não zero na linha atual.
        for j in range(m):
            # Loop através das colunas da linha atual (de 0 até m-1)
            if matriz[i][j] != 0:
                # Se o elemento da matriz na posição [i][j] for diferente de zero...
                if j <= indice_coluna_anterior:
                    # Verifica se o índice do primeiro elemento não zero desta linha é menor ou igual
                    # ao índice do elemento não zero encontrado na linha anterior.
                    # Se isso acontecer, a matriz não está em forma de escada, então retornamos 'N'.
                    return 'N'
                indice_coluna_anterior = j
                # Atualiza o índice da coluna do último elemento não zero encontrado.
                encontrou_nao_zero = True
                # Marca que encontrou um elemento não zero na linha atual.
                break
                # Sai do loop interno, já que só precisamos do primeiro elemento não zero da linha.
        if not encontrou_nao_zero and indice_coluna_anterior != m - 1:
            # Se não encontrou nenhum elemento não zero na linha atual e a última coluna não foi preenchida com elementos não zero
            # A matriz deve ser composta apenas de zeros nas linhas seguintes (abaixo desta).
            for k in range(i + 1, n):
                # Verifica as linhas restantes da matriz (da linha i+1 até a última linha)
                if any(matriz[k][l] != 0 for l in range(m)):
                    # Se encontrar algum elemento não zero em qualquer linha subsequente, retorna 'N',
                    # pois isso significa que a matriz não está na forma escalonada.
                    return 'N'
            break
            # Se todas as linhas subsequentes forem zero, sai do loop principal.
    return 'S'
    # Se todos os critérios forem atendidos, a matriz está na forma escalonada, então retorna 'S'.
n, m = map(int, input().strip().split())
# Lê dois inteiros da entrada (n e m), onde n é o número de linhas e m é o número de colunas da matriz.
matriz = []
# Inicializa uma lista vazia que armazenará a matriz.
for i in range(n):
    # Loop para ler cada linha da matriz (n linhas no total).
    linha = list(map(int, input().strip().split()))
    # Lê uma linha da entrada, transforma em uma lista de inteiros e armazena na variável 'linha'.
    matriz.append(linha)
    # Adiciona a linha lida à matriz.
print(verificar_matriz_escada(n, m, matriz))
# Chama a função verificar_matriz_escada passando os valores de n, m e a matriz lida como parâmetros.
# Imprime o resultado retornado pela função ('S' ou 'N').
