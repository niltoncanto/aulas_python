# Importações necessárias
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Classe abstrata Evento
class Evento(ABC):
    def __init__(self, nome, data, preco_base):
        self._nome = nome
        self._data = data
        self._preco_base = preco_base
        self._descontos = []

    @abstractmethod
    def preco_ingresso(self):
        pass

    @abstractmethod
    def aplicar_desconto(self):
        pass

    def get_info(self):
        return f"Evento: {self._nome}, Data: {self._data}, Preço Base: R${self._preco_base}"

    def adicionar_desconto(self, desconto):
        self._descontos.append(desconto)

    def calcular_preco_final(self):
        preco_final = self.preco_ingresso()
        for desconto in self._descontos:
            preco_final -= desconto.calcular_desconto(self._preco_base)
        return max(preco_final, 0)

# Classe Concreta PecaTeatro
class PecaTeatro(Evento):
    def preco_ingresso(self):
        # Lógica específica para calcular o preço do ingresso de uma peça de teatro
        return self._preco_base * 1.1  # Acréscimo de 10%

    def aplicar_desconto(self):
        # Implementação de descontos específicos para peças de teatro
        pass

# Classe Concreta ConcertoMusical
class ConcertoMusical(Evento):
    def preco_ingresso(self):
        # Lógica específica para calcular o preço do ingresso de um concerto musical
        return self._preco_base * 1.2  # Acréscimo de 20%

    def aplicar_desconto(self):
        # Implementação de descontos específicos para concertos musicais
        pass

# Classe Sala
class Sala:
    def __init__(self, nome, capacidade):
        self._nome = nome
        self._capacidade = capacidade
        self._eventos = []

    def adicionar_evento(self, evento):
        if isinstance(evento, Evento):
            self._eventos.append(evento)
            return True
        return False

    def listar_eventos(self):
        for evento in self._eventos:
            print(evento.get_info())

# Classe Desconto 
class Desconto(ABC):
    @abstractmethod
    def calcular_desconto(self, preco_base):
        pass

# Classe DescontoEstudante
class DescontoEstudante(Desconto):
    def calcular_desconto(self, preco_base):
        return preco_base * 0.2  # Desconto de 20% para estudantes

# Main para testar o sistema
if __name__ == "__main__":
    sala = Sala("Sala Principal", 200)
    evento1 = PecaTeatro("Hamlet", "2024-05-25", 100)
    evento2 = ConcertoMusical("The Beatles Cover", "2024-06-10", 150)

    desconto_estudante = DescontoEstudante()

    evento1.adicionar_desconto(desconto_estudante)
    evento2.adicionar_desconto(desconto_estudante)

    sala.adicionar_evento(evento1)
    sala.adicionar_evento(evento2)

    sala.listar_eventos()

    print(f"Preço final (Peça de Teatro): R${evento1.calcular_preco_final()}")
    print(f"Preço final (Concerto Musical): R${evento2.calcular_preco_final()}")
