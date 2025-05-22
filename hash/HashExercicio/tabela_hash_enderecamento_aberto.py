# Define a classe da tabela hash usando endereçamento aberto
class TabelaHashAberta:
    # Construtor da classe
    def __init__(self, tamanho):
        # Cria a tabela com o tamanho especificado, preenchida com None (posições vazias)
        self.tabela = [None] * tamanho
        # Armazena o tamanho da tabela para uso em outros métodos
        self.tamanho = tamanho

    # Função hash: calcula o índice da tabela para uma chave
    def hash(self, chave):
        # Usa o operador módulo para garantir que o índice esteja dentro dos limites da tabela
        return chave % self.tamanho

    # Método para inserir uma chave na tabela
    def inserir(self, chave):
        # Calcula a posição inicial usando a função hash
        posicao = self.hash(chave)

        # Salva a posição original para detectar se voltamos ao ponto inicial (evita loop infinito)
        original = posicao

        # Contador de tentativas (número de colisões resolvidas até encontrar posição livre)
        passos = 0

        # Enquanto a posição atual da tabela estiver ocupada, tenta a próxima posição (sondagem linear)
        while self.tabela[posicao] is not None:
            print(f"Colisão na posição {posicao} para a chave {chave}. Tentando próxima posição...")
            
            # Avança para a próxima posição (com wrap-around circular usando módulo)
            posicao = (posicao + 1) % self.tamanho
            passos += 1

            # Se voltarmos à posição original, a tabela está cheia e não é possível inserir
            if posicao == original:
                print("Tabela cheia!")
                return  # Encerra a inserção

        # Quando encontra uma posição livre, insere a chave
        print(f"Chave {chave} inserida na posição {posicao} após {passos} tentativas.")
        self.tabela[posicao] = chave  # Salva a chave na posição encontrada

    # Método para exibir o conteúdo atual da tabela
    def exibir(self):
        # Percorre todos os índices da tabela e imprime o conteúdo de cada um
        for i, valor in enumerate(self.tabela):
            print(f"{i}: {valor}")

# Bloco principal para testar a tabela hash com endereçamento aberto
if __name__ == "__main__":
    # Cria uma tabela hash com 7 posições
    tabela = TabelaHashAberta(7)

    # Lista de chaves a serem inseridas (várias gerarão colisões com h(k) = k % 7)
    chaves = [10, 3, 17, 24, 31]

    print("Inserindo chaves na tabela hash:")
    for chave in chaves:
        tabela.inserir(chave)

    print("\nTabela final:")
    tabela.exibir()
