from abc import ABC, abstractmethod
from enum import Enum

class Status(Enum):
    DISPONIVEL = 1
    RESERVADO = 2

class Livro(ABC):
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = Status.DISPONIVEL
        
    def to_string(self):
        return f"{self.titulo};{self.autor};{self.ISBN};{self.status}"
    
    @abstractmethod
    def reservar(self):
        pass

    def devolver(self):
        self.status = Status.DISPONIVEL
