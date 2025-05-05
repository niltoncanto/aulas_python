def jogar_cartas_fora(n):
    fila = list(range(1, n + 1))  # Cria a fila de cartas de 1 a n
    descartadas = []

    while len(fila) > 1:
        descartada = fila.pop(0)
        descartadas.append(descartada)  # Remove e descarta a primeira carta
        topo = fila.pop(0)
        fila.append(topo)  # Move a próxima carta para o final da fila

    return descartadas, fila[0]  # Retorna as cartas descartadas e a última carta

def main():
    while True:
        n = int(input())  # Lê o número de cartas
        if n == 0:
            break  # Se for 0, encerra o programa

        descartadas, ultima = jogar_cartas_fora(n)

        # Exibe as cartas descartadas
        if descartadas:
            print(f"Discarded cards: {', '.join(map(str, descartadas))}")
        else:
            print("Discarded cards:")

        # Exibe a última carta restante
        print(f"Remaining card: {ultima}")

# Executa o programa
if __name__ == "__main__":
    main()
