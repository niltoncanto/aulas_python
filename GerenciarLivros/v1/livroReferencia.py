from livro import Livro
from enum import Enum

class Tema(Enum):
    FISICA = "Física"
    QUIMICA = 'Química'

class LivroReferencia(Livro):
    def __init__(self, titulo, autor, ISBN, tema):
        super().__init__(titulo, autor, ISBN)
        self.tema = tema

    def reservar(self):
        return "Livros de referência não podem ser reservados."
