
from abc import ABC, abstractmethod 
from enum import Enum

#tipo de dados que representa o status do livro
class Status(Enum):
    DISPONIVEL = "Reservado"

class Tema(Enum):
    FISICA = "FISICA"
    QUIMICA = "QUIMICA"

#classe abstrata extende ABC (abstract class)
class Livro(ABC):
    #método contrutor da classe Livro
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.status = Status.DISPONIVEL
        self.dataDevolucao = None
        self.tema = None

    @abstractmethod
    def reservar():
        raise NotImplementedError("O método reservar deve ser implementado nas subclasses")
    
    #método de instancia (concreto)
    def devolver(self):
        self.status = Status.DISPONIVEL
        return "Devolucao efetuada"
    
    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.isbn}, {self.status}, {self.dataDevolucao}, {self.tema}"


