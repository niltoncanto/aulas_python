from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia,Tema
from livro import Livro
from usuario import Usuario
from gerenciararquivo import GerenciarArquivo
livro1 = LivroPadrao("xxx","John",444444)
livro2 = LivroReferencia("xxx","John",444444,Tema.FISICA)
usuario = Usuario(20000,"John")
print("**início****")
print(usuario.fazerReserva(livro1))
print(usuario.fazerReserva(livro2))
print(usuario.fazerDevolucao(livro1))
arq = GerenciarArquivo("teste1.txt")
arq.gravarArq(usuario.fazerReserva(livro1) + '\n')
arq.gravarArq(usuario.fazerReserva(livro2) + '\n')
print("******")
print(arq.lerArq())

print("***Linha***")
print(arq.lerLinha())

print("***Linhas***")
print(arq.lerLinhas())

print("***Linhas while***")
print(arq.lerWhile())

