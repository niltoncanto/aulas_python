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
# ######################################
class LivroPadrao(Livro):
    def __init__(self, titulo, autor, ISBN):
        super().__init__(titulo, autor, ISBN)
        self.dataDeDevolucao = datetime.now() + timedelta(days=7)

    def to_string(self):
        return super().to_string() + "Padrão";self.dataDeDevolucao
        
    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.RESERVADO
            return "Livro reservado com sucesso."
        else:
            return "Livro já está reservado."
        
# ############################
class LivroReferencia(Livro):
    def __init__(self, titulo, autor, ISBN, tema):
        super().__init__(titulo, autor, ISBN)
        self.tema = tema

    def to_string(self):
        return super().to_string() + "Referencia";self.tema
    
    def reservar(self):
        return "Livros de referência não podem ser reservados."
# ############################
class Usuario:
    ID = 10000
    def __init__(self, nome):
        self.nome = nome
        Usuario.ID += 1

    def to_string(self):
        return f"{self.nome};{self.ID}\n"

    def fazerReserva(self, livro):
        print(livro.reservar())
# ############################