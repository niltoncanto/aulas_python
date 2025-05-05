from abc import ABC,abstractmethod
from enum import Enum

class Status(Enum):
    DISPONIVEL = 'Disponível'
    RESERVADO = 'Reservado'

class Livro(ABC):
    def __init__(título,autor,isbn):
        self.status = Status.DISPONIVEL
        
    @abstractmethod
    def reservar(self):
        raise NotImplementedError("O método reservar deve ser implementado nas subclasses.")