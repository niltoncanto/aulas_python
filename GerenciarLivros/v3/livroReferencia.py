from livro import Livro
from enum import Enum

class Tema(Enum):
    QUIMICA = "química"
    FISICA = "física"

class LivroReferencia(Livro):
    def __init__(self, titulo, autor, isbn,tema):
        super().__init__(titulo, autor, isbn)
        self.tema = tema
        
    def reservar(self):
        return "Livros referência não podem ser reservados."
    
    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.isbn}, {self.status}, {self.tema}"