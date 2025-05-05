# Classe Livro: Deve conter os seguintes atributos:
# 	titulo: Representa o título do livro.
# 	autor: Representa o autor do livro.
# 	ano_publicacao: Representa o ano de publicação do livro.

# Método mostrar_info(): Deve imprimir as informações do livro.

# Classe Biblioteca: Deve conter os seguintes atributos:
# 	livros: Um array ou lista para armazenar os objetos da classe Livro.
# 	capacidade: Representa a capacidade máxima de livros que a biblioteca pode ter.
# Método adicionar_livro(livro): Deve adicionar um livro à biblioteca, considerando a capacidade.
# Método mostrar_livros(): Deve imprimir as informações de todos os livros na biblioteca.

# Crie um programa que instancie alguns livros e uma biblioteca e utilize seus métodos para adicionar os livros e mostrar as informações.
class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def mostrarInfo(self):
        return f"Título:{self.titulo}\nAutor:{self.autor}\nAno:{self.ano_publicacao}\n"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.capacidade = 1000
    
    def adicionarLivros(self,livro):
        if len(self.livros)<self.capacidade:
            self.livros.append(livro)
            return "Livro inserido com sucesso!"
        else:
            return "Biblioteca cheia!"

    def mostrar_livros(self):
        for i in self.livros:
            print(i.mostrarInfo())

biblioteca = Biblioteca()
livro1 = Livro("XXX","John",2000)
livro2 = Livro("BBB","João",2010)
biblioteca.adicionarLivros(livro1)
biblioteca.adicionarLivros(livro2)
biblioteca.mostrar_livros()





