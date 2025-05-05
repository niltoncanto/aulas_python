from abc import ABC,abstractmethod
from enum import Enum

#lista de constantes 
class Status(Enum):
    DISPONIVEL = "disponível"
    RESERVADO = "reservado"
    

#classe abstrata não pode ser instanciada
class Livro(ABC):
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.status = Status.DISPONIVEL
    
    #Método abstrato deve obrigatoriamente ser 
    #implementado nas subclasses
    @abstractmethod    
    def reservar():
        raise NotImplementedError("Metodo abstrado deve ser implementado na subclasse")
    
    #método concreto
    def devolver(self):
        self.status = Status.DISPONIVEL
        return "Devolução efetuada"