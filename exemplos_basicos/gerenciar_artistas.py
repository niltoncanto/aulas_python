from abc import ABC, abstractmethod

# Classe Artista
class Artista:
    def __init__(self, nome, genero_musical, ano_inicio):
        self.__nome = nome
        self.__genero_musical = genero_musical
        self.__ano_inicio = ano_inicio

    # Getters e Setters # vc poderia ter utilizado também @property
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_genero_musical(self):
        return self.__genero_musical

    def set_genero_musical(self, genero_musical):
        self.__genero_musical = genero_musical

    def get_ano_inicio(self):
        return self.__ano_inicio

    def set_ano_inicio(self, ano_inicio):
        self.__ano_inicio = ano_inicio

    # Sobrescrita do método __str__ para representação em String do Objeto
    def __str__(self):
        return f"Artista: {self.__nome}, Gênero: {self.__genero_musical}, Ano de Início: {self.__ano_inicio}"

# Classe GerenteDeArtistas
class GerenteDeArtistas:
    def __init__(self):
        self.__artistas = [] #cada gerente tem uma lista

    def adicionar_artista(self, artista):
        self.__artistas.append(artista) 

    def listar_artistas(self):
        for artista in self.__artistas:
            print(artista) 

    def atualizar_artista(self, nome, novos_dados):
        for artista in self.__artistas:
            if artista.get_nome() == nome:
                artista.set_nome(novos_dados.get('nome', artista.get_nome()))
                artista.set_genero_musical(novos_dados.get('genero_musical', artista.get_genero_musical()))
                artista.set_ano_inicio(novos_dados.get('ano_inicio', artista.get_ano_inicio()))
                print(f"Informações do artista {nome} atualizadas com sucesso!")
                return None
        print(f"Artista {nome} não encontrado.")


# Classe ArtistaDestaque (só para treinar o uso de Herança e Polimorfismo)
class ArtistaDestaque(Artista):
    def __init__(self,artista,premios_recebidos):
        self.__premios_recebidos = premios_recebidos
        super().__init__(artista.get_nome(),artista.get_genero_musical(),artista.get_ano_inicio())

    def __str__(self):
        premios = ', '.join(self.__premios_recebidos) # o join é usado para concatenar os itens de uma lista, por exemplo, vc tem uma lista de palavras e quer transformar em uma frase única.
        return super().__str__() + f", Prêmios Recebidos: {premios}" #aqui estamos subscrevendo o método __str__ mas aproveitando o que já temos na super classe.


# Classe Abstrata OperacaoSistema
# serve como uma abstração que define uma interface comum para todas as operações do sistema.    
class OperacaoSistema(ABC):
    @abstractmethod
    def executar_operacao(self):
        pass

# Classes concretas para Operações do Sistema
# representa uma operação específica no sistema (AdicionarArtista, ListarArtistas, AtualizarArtista). 
# permite a especialização de comportamentos, onde cada operação pode ter uma implementação única, mantendo o código organizado e modular.
# As subclasses encapsulam o comportamento específico de uma operação.
class AdicionarArtista(OperacaoSistema):
    def __init__(self, gerente, artista):
        self.gerente = gerente
        self.artista = artista

    def executar_operacao(self):
        self.gerente.adicionar_artista(self.artista)

class ListarArtistas(OperacaoSistema):
    def __init__(self, gerente):
        self.gerente = gerente

    def executar_operacao(self):
        self.gerente.listar_artistas()

class AtualizarArtista(OperacaoSistema):
    def __init__(self, gerente, nome, novos_dados):
        self.gerente = gerente
        self.nome = nome
        self.novos_dados = novos_dados

    def executar_operacao(self):
        self.gerente.atualizar_artista(self.nome, self.novos_dados)

# Exemplo de Uso
if __name__ == "__main__":
    #bCRIAÇÃO DOS ARTISTAS
    artista1 = Artista("Artista 1", "Rock", 2000)
    artista2 = Artista("Artista 2", "Pop", 1980)
    artista3 = Artista("Artista 3", "MPB", 2010)

    #CRIAÇÃO DOS GERENTES DE ARTISTAS
    gerente1 = GerenteDeArtistas() #cria um gerente1
    gerente2 = GerenteDeArtistas() #cria um gerente2

    #ATRIBUI O ARTISTA AO GERENTE ATRAVÉS DA CLASSE AUXILIAR AdicionarArtista
    adicionar_artista1 = AdicionarArtista(gerente1, artista1) #cria o objeto adicionar_artista1
    adicionar_artista2 = AdicionarArtista(gerente1, artista2) #cria o objeto adicionar_artista2
    adicionar_artista3 = AdicionarArtista(gerente2, artista3) #cria o objeto adicionar_artista3
    print("\n")

    #após criar os objtos adicionar artista, chama o método executar_operacao    
    adicionar_artista1.executar_operacao()
    adicionar_artista2.executar_operacao()
    adicionar_artista3.executar_operacao()
    
  
    #CRIAÇÃO DO ARTISTAS DESTAQUE
    artista_destaque = ArtistaDestaque(artista2, ["Prêmio 1", "Prêmio 2"]) #crio o objeto artista_destaque
    adicionar_artista_destaque = AdicionarArtista(gerente1, artista_destaque) #adiciono o objeto artista_destaque na lista do gerente1 através da classe AdicionarArtista

    adicionar_artista_destaque.executar_operacao()

    print("** Artistas Gerente 1 **")
    listar1 = ListarArtistas(gerente1) #cria o objeto da classe ListarArtistas
    listar1.executar_operacao()
    print("")

    print("** Artistas Gerente 2 **")
    listar2 = ListarArtistas(gerente2) #cria o objeto da classe ListarArtistas
    listar2.executar_operacao()
    print("")

    print("** Teste atualização de Artistas **")
    atualizar_artista1 = AtualizarArtista(gerente1, "Artista 1", {"nome": "Artista 1 Atualizado"}) #cria o objeto AtualizarArtista1
    atualizar_artista1.executar_operacao()
    print("") 
    atualizar_artista2 = AtualizarArtista(gerente1, "Artista 5", {"nome": "Artista 1 Atualizado"}) #cria o objeto AtualizarArtista2
    atualizar_artista2.executar_operacao() # vai falhar, "Artista 5" não foi criado!
    print("")
  
