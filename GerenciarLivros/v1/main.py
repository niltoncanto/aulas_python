from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia
from usuario import Usuario
from livroReferencia import Tema

def main():
    livro1 = LivroPadrao("O Senhor dos Anéis", "J.R.R. Tolkien", "123456")
    livro2 = LivroReferencia("Enciclopédia", "Vários Autores", "789012", Tema.FISICA)

    usuario1 = Usuario("João", 1)

    print(usuario1.fazerReserva(livro1))
    print(usuario1.fazerReserva(livro2))
    print(usuario1.fazerDevolucao(livro1))

    print(Livro.reservar())


if __name__ == "__main__":
    main()
