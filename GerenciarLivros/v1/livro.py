from enum import Enum
from abc import ABC,abstractmethod

class Status(Enum):
    DISPONIVEL = "Disponível"
    RESERVADO = "Reservado"

#intanciando uma classe abstrata
class Livro(ABC):
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = Status.DISPONIVEL

    @abstractmethod
    def reservar(self):
        raise NotImplementedError("O método reservar deve ser implementado nas subclasses")
    
    def devolver(self):
        self.status = Status.DISPONIVEL
        return "Devolução efetivada"