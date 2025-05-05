

from persistencia_dados import GerenciadorDePersistencia
from livro_padrao import LivroPadrao
from livro_referencia import LivroReferencia
from usuario import Usuario

def main():
    # Criação de livros e usuários
    gerenciador = GerenciadorDePersistencia()
    livro1 = LivroPadrao("Python 101", "José Silva", "123ABC")
    gerenciador.salvar_livro(livro1)
    livro2 = LivroReferencia("Enciclopédia Python", "Maria Oliveira", "456DEF", "Programação")
    gerenciador.salvar_livro(livro2)
    usuario1 = Usuario("João")
    gerenciador.salvar_usuario(usuario1)
    usuario2 = Usuario("Maria")
    gerenciador.salvar_usuario(usuario2)

    # reserva
    usuario1.fazerReserva(livro1)
    usuario1.fazerReserva(livro2)

    # Devolução
    livro1.devolver()
    usuario1.fazerReserva(livro1)

    livros = GerenciadorDePersistencia.carregar_livros()

    usuarios = GerenciadorDePersistencia.carregar_usuarios()
    print(f"usuarios:{usuarios}")



if __name__ == "__main__":
    main()
