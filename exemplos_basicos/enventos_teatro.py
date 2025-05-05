# Classe abstrata Evento
from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nome, data, preco_base):
        self.__nome = nome
        self.__data = data
        self.__preco_base = preco_base

    @abstractmethod
    def preco_ingresso(self):
        pass

    def get_info(self):
        return f"Evento: {self.__nome}, Data: {self.__data}, Preço Base: R${self.__preco_base}"

# Classe Sala
class Sala:
    def __init__(self, nome, capacidade):
        self.__nome = nome
        self.__capacidade = capacidade
        self.__eventos = []

    def adicionar_evento(self, evento):
        if isinstance(evento, Evento) and len(self.__eventos) < self.__capacidade:
            self.__eventos.append(evento)
            return True
        return False

    def listar_eventos(self):
        for evento in self.__eventos:
            print(evento.get_info())
