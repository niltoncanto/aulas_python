n = int(input())
anos_transcorridos = []
resultados = []
for i in range(n):
  anos_transcorridos.append(int(input()))

for T in anos_transcorridos:
  if T < 2015:
    # Se o evento aconteceu D.C., calculamos o ano subtraindo de 2015
    ano_evento = 2015 - T
    resultados.append(f"{ano_evento} D.C.")
  else:
    # Se o evento aconteceu A.C., calculamos o ano e consideramos a inexistência do ano 0
    ano_evento = T - 2015 + 1
    resultados.append(f"{ano_evento} A.C.")

for resultado in resultados:
    print(resultado)