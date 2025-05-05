from abc import ABC, abstractmethod

# Classe Abstrata: Restaurante
class Restaurante(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.avaliacoes = {}

    def adicionarAvaliacao(self, data, nota):
        """
        Adiciona uma avaliação ao restaurante.

        Args:
            data (str): Data da avaliação.
            nota (int): Nota da avaliação.
        """
        self.avaliacoes[data] = nota

    @abstractmethod
    def calcularMedia(self):
        """
        Método abstrato para calcular a média das avaliações.
        """
        pass

    def getNome(self):
        """
        Retorna o nome do restaurante.
        """
        return self.nome

# Subclasse: FastFood
class FastFood(Restaurante):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo

    def calcularMedia(self):
        """
        Calcula a média das avaliações de FastFood (soma das notas dividido pelo número de avaliações).
        """
        if len(self.avaliacoes) == 0:
            return 0
        return sum(self.avaliacoes.values()) / len(self.avaliacoes)

# Subclasse: FineDining
class FineDining(Restaurante):
    def __init__(self, nome, estrelasMichelin):
        super().__init__(nome)
        self.estrelasMichelin = estrelasMichelin

    def calcularMedia(self):
        """
        Calcula a média das avaliações de FineDining.
        Se o restaurante tiver estrelas Michelin, cada estrela adiciona 0.5 à média final.
        """
        if len(self.avaliacoes) == 0:
            return 0
        media = sum(self.avaliacoes.values()) / len(self.avaliacoes)
        if self.estrelasMichelin > 0:
            media += 0.5 * self.estrelasMichelin
        return media

# Enum: TipoFastFood
class TipoFastFood(Enum):
    HAMBURGUER = "Hamburguer"
    PIZZA = "Pizza"
    SANDUICHE = "Sanduiche"

# Classe: GerenciarArquivo
class GerenciarArquivo:
    @staticmethod
    def gravar(dados):
        """
        Grava os dados (nome e avaliações) do restaurante em um arquivo .txt.

        Args:
            dados (dict): Dados do restaurante a serem gravados.
        """
        try:
            with open('restaurante.txt', 'w') as arquivo:
                for chave, valor in dados.items():
                    arquivo.write(f'{chave}: {valor}\n')
        except Exception as e:
            print(f"Erro ao gravar arquivo: {e}")

    @staticmethod
    def ler():
        """
        Lê os dados do arquivo .txt e retorna um objeto Restaurante.
        """
        restaurante = None
        try:
            with open('restaurante.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                nome = linhas[0].strip().split(': ')[1]
                tipo = linhas[1].strip().split(': ')[1]
                estrelas = linhas[2].strip().split(': ')[1]
                avaliacoes = {}
                for linha in linhas[3:]:
                    data, nota = linha.strip().split(': ')
                    avaliacoes[data] = int(nota)
                if tipo == TipoFastFood.HAMBURGUER.value:
                    restaurante = FastFood(nome, TipoFastFood.HAMBURGUER)
                elif tipo == TipoFastFood.PIZZA.value:
                    restaurante = FastFood(nome, TipoFastFood.PIZZA)
                elif tipo == TipoFastFood.SANDUICHE.value:
                    restaurante = FastFood(nome, TipoFastFood.SANDUICHE)
                elif int(estrelas) > 0:
                    restaurante = FineDining(nome, int(estrelas))
                restaurante.avaliacoes = avaliacoes
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
        return restaurante

# Classe: Main
if __name__ == "__main__":
    # Cria instâncias de restaurantes
    fast_food = FastFood("Fast Food Express", TipoFastFood.HAMBURGUER)
    fine_dining = FineDining("Fancy Dining", 3)

    # Adiciona avaliações
    fast_food.adicionarAvaliacao("2023-09-26", 4)
    fine_dining.adicionarAvaliacao("2023-09-27", 5)
    
    # Calcula a média
    media_fast_food = fast_food.calcularMedia()
    media_fine_dining = fine_dining.calcularMedia()

    # Exibe resultados
    print(f"Restaurante: {fast_food.getNome()} (Tipo: {fast_food.tipo})")
    print(f"Média de Avaliações: {media_fast_food:.2f}\n")

    print(f"Restaurante: {fine_dining.getNome()} (Estrelas Michelin: {fine_dining.estrelasMichelin})")
    print(f"Média de Avaliações: {media_fine_dining:.2f}\n")

    # Grava os dados em um arquivo
    dados_restaurante = {
        "Nome": fine_dining.getNome(),
        "Tipo": TipoFastFood.HAMBURGUER.value,
        "Estrelas Michelin": 3,
        "Avaliações": fine_dining.avaliacoes
    }
    GerenciarArquivo.gravar(dados_restaurante)

    # Lê os dados do arquivo e exibe
    restaurante_recuperado = GerenciarArquivo.ler()
    if restaurante_recuperado:
        print("Dados do restaurante recuperados do arquivo:")
        print(f"Restaurante: {restaurante_recuperado.getNome()} (Tipo: {restaurante_recuperado.tipo})")
        print(f"Avaliações: {restaurante_recuperado.avaliacoes}")
