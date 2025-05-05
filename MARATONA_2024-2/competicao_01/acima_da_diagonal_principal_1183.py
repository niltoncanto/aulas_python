# Solicita ao usuário que insira o tipo de operação ('S' para soma ou 'M' para média)
operacao = input()

# Cria uma matriz 12x12 inicializada com zeros
matriz = [ [0] * 12 for i in range(12)]

# Preenche a matriz com valores de ponto flutuante fornecidos pelo usuário
for i in range(12):
  for j in range(12):
    matriz[i][j] = float(input())

# A matriz é criada e agora contém todos os valores inseridos pelo usuário

# Inicializa as variáveis cont e soma para armazenar o número de elementos a serem somados e a soma desses elementos, respectivamente
cont = 0
soma = 0

# Itera sobre cada elemento da matriz para calcular a soma e contar os elementos acima da diagonal principal
for i in range(12):
  for j in range(12):
      # Verifica se o elemento está acima da diagonal principal (j > i)
      if j > i:
        soma += matriz[i][j]  # Adiciona o valor do elemento à soma total
        cont += 1  # Incrementa o contador de elementos

# Verifica a operação solicitada pelo usuário
if operacao == 'S':
  # Se a operação for soma, imprime a soma dos elementos acima da diagonal principal
  print(f"{soma:.1f}")
elif operacao == 'M':
  # Se a operação for média, calcula a média dos elementos acima da diagonal principal
  media = soma / cont
  # Imprime a média, formatada com uma casa decimal
  print(f"{media:.1f}")