import datetime
from livro import Status,Tema
from livroPadrao import LivroPadrao
from livroReferencia import LivroReferencia

class Bibliotecario:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def adicionar_livro(self, livro):
        with open(self.arquivo, 'a') as file:
            file.write(str(livro) + '\n')

    def emprestar_livro(self, isbn, usuario):
        livros = self._ler_livros()
        for livro in livros:
            print(livro)
            print("***")
            if livro.isbn == isbn and livro.status == Status.DISPONIVEL:
                livro.usuario = str(usuario)
                livro.data_devolucao = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
                self._gravar_livros(livros)
                return "Livro reservado com sucesso!"
        return "Livro não disponível ou não encontrado."

    def devolver_livro(self, isbn):
        livros = self._ler_livros()
        for livro in livros:
            if livro.isbn == isbn and livro.status == "Reservado":
                livro.status = "Disponível"
                livro.data_devolucao = None
                self._gravar_livros(livros)
                return "Livro devolvido com sucesso!"
        return "Livro não encontrado ou já estava disponível."

    def _ler_livros(self):
        livros = []
        with open(self.arquivo, 'r') as file:
            for line in file:
                titulo, autor, isbn, status, data_devolucao,tema = line.strip().split(', ')
                if tema==None:
                    livro = LivroPadrao(titulo, autor, isbn)
                    livro.data_devolucao = data_devolucao if data_devolucao != "None" else None
                else:
                    livro = LivroReferencia(titulo, autor, isbn,tema)
                    livro.tema = tema
                
                livro.status = status
                livros.append(livro)
        return livros

    def _gravar_livros(self, livros):
        with open(self.arquivo, 'w') as file:
            for livro in livros:
                file.write(str(livro) + '\n')
