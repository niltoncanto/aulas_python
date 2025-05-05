from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia,Tema
from livro import Livro
from usuario import Usuario
from arquivo import Arquivo


livro1 = LivroPadrao("ABC","John",54321)
livro2 = LivroReferencia("YYY","Maria",12345,Tema.FISICA)
usuario = Usuario(20000,"Mario")
print(usuario.fazerReserva(livro1))
print(usuario.fazerReserva(livro2))
print(usuario.fazerDevolucao(livro1))

livrosTXT = Arquivo("livros.txt")
livrosTXT.gravar(str(livro1))
livrosTXT.gravar(str(livro2))
texto = livrosTXT.ler()
print("Método Ler")
print(texto)

usuarios = Arquivo("usuarios.txt")
usuarios.gravar(str(usuario))


texto = livrosTXT.lerLinha()
print("LerLinha")
print(texto)

texto = livrosTXT.lerLinhas()
print("LerLinhas")
print(texto)

texto = livrosTXT.lerTudo()
print("LerTudo")
print(texto)

texto = livrosTXT.lerWhile()
print("LerWhile")
print(texto)
