# Inicializa uma lista vazia para armazenar os números
lista = []

# Loop que itera 4 vezes para coletar 4 números do usuário
for i in range(4):
  # Solicita um número do usuário, converte para inteiro e adiciona à lista
  lista.append(int(input("Digite um número: ")))

# Calcula a diferença conforme especificado: (primeiro número * segundo número) - (terceiro número * quarto número)
DIFERENCA = (lista[0] * lista[1] - lista[2] * lista[3])

# Imprime o resultado na tela
print(f"DIFERENCA = {DIFERENCA}")