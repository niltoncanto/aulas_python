from collections import deque
def jogar_cartas_fora(n):
    fila = deque(range(1, n + 1))  # Cria a fila de cartas de 1 a n
    descartadas = []

    while len(fila) > 1:
        descartadas.append(fila.popleft())  # Remove e descarta a primeira carta
        fila.append(fila.popleft())  # Move a próxima carta para o final da fila

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
