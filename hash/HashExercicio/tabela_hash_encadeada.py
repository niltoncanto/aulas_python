# Tabela hash com encadeamento separado (listas ligadas)
# Define a classe que representa a Tabela Hash com Encadeamento Separado
class TabelaHashEncadeada:
    
    # Construtor da classe - inicializa a tabela com listas vazias
    def __init__(self, tamanho):
        # Armazena o tamanho total da tabela
        self.tamanho = tamanho

        # Inicializa a tabela como uma lista vazia
        self.tabela = []

        # Adiciona uma lista vazia para cada posição (bucket)
        for _ in range(tamanho):
            self.tabela.append([])

    # Função hash simples: retorna o índice correspondente à chave
    def hash(self, chave):
        return chave % self.tamanho

    # Método para inserir uma chave na tabela
    def inserir(self, chave):
        # Calcula a posição onde a chave deve ser inserida
        posicao = self.hash(chave)
        # Adiciona a chave à lista do bucket correspondente
        self.tabela[posicao].append(chave)
        # Mostra mensagem indicando em qual bucket a chave será inserida
        print(f"Chave {chave} inserida no bucket {posicao}.")

    # Método para buscar uma chave na tabela
    def buscar(self, chave):
        # Calcula em qual bucket a chave estaria
        posicao = self.hash(chave)
        print(f"Buscando chave {chave} no bucket {posicao}...")
        
        # Percorre a lista do bucket em busca da chave
        for valor in self.tabela[posicao]:
            print(f"Verificando {valor}")
            if valor == chave:
                print("Chave encontrada!")
                return True  # Retorna True se encontrar a chave
        
        # Se não encontrar a chave, informa isso e retorna False
        print("Chave não encontrada.")
        return False

    # Método para exibir o conteúdo completo da tabela
    def exibir(self):
        # Percorre todos os índices (buckets) da tabela
        for i, lista in enumerate(self.tabela):
            # Imprime o conteúdo de cada bucket
            print(f"{i}: {lista}")


# Bloco principal de execução
if __name__ == "__main__":
    # Cria uma tabela hash com 7 buckets
    tabela = TabelaHashEncadeada(7)

    # Insere uma lista de chaves na tabela
    for chave in [14, 21, 7, 28, 35, 40, 66]:
        tabela.inserir(chave)

    # Exibe o conteúdo final da tabela
    print("\nTabela final:")
    tabela.exibir()

    # Busca pela chave 28
    print("\nBusca pela chave 28:")
    tabela.buscar(28)
    # Busca pela chave 100  
    print("\nBusca pela chave 77:")
    tabela.buscar(77)

""" 
Observações didáticas:
A função hash é modular (% tamanho) para garantir que o índice sempre esteja no intervalo da tabela.
O uso de listas ([]) por bucket implementa o encadeamento separado.
O loop for valor in self.tabela[posicao] simula a verificação linear da lista em caso de colisões.
O método exibir() ajuda a visualizar a distribuição das chaves nos buckets.
 """