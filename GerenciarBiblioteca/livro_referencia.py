from livro import Livro

class LivroReferencia(Livro):
    def __init__(self, titulo, autor, ISBN, tema):
        super().__init__(titulo, autor, ISBN)
        self.tema = tema

    def to_string(self):
        return super().to_string() + "Referencia";self.tema
    
    def reservar(self):
        return "Livros de referência não podem ser reservados."
