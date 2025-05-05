'''
Enunciado:  Você foi encarregado de criar um sistema para gerenciar uma biblioteca. O sistema deve ser capaz de adicionar livros, 
limitando a quantidade com base na capacidade fornecida, e mostrar todos os livros cadastrados. Implemente o sistema usando duas classes: 
Livro e Biblioteca.

Classe Livro: Deve conter os seguintes atributos:
	titulo: Representa o título do livro.
	autor: Representa o autor do livro.
	ano_publicacao: Representa o ano de publicação do livro.
Método mostrar_info(): Deve imprimir as informações do livro.

Classe Biblioteca: Deve conter os seguintes atributos:
	livros: Um array ou lista para armazenar os objetos da classe Livro.
	capacidade: Representa a capacidade máxima de livros que a biblioteca pode ter.

Método adicionar_livro(livro): Deve adicionar um livro à biblioteca, considerando a capacidade.
Método remover_livro(livro): Deve remover um livro à biblioteca.
Método mostrar_livros(): Deve imprimir as informações de todos os livros na biblioteca.

Crie um programa que instancie alguns livros e uma biblioteca e utilize seus métodos para adicionar os livros e mostrar as informações.
'''
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

class Biblioteca:
    def __init__(self, capacidade):
        self.livros = []
        self.capacidade = capacidade

    def adicionar_livro(self, livro):
        if len(self.livros) < self.capacidade:
            self.livros.append(livro)
        else:
            print("A biblioteca está cheia!")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
        else:
            print("Livro não encontrado!")

    def mostrar_livros(self):
        for livro in self.livros:
            livro.mostrar_info()
            print()
if __name__ == "__main__":
    l1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    l2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
    l3 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)

    b1 = Biblioteca(2)
    b1.adicionar_livro(l1)
    b1.adicionar_livro(l2)
    b1.adicionar_livro(l3)

    b1.mostrar_livros()
    print()

    b1.remover_livro(l2)
    b1.mostrar_livros()
    print()

    b1.adicionar_livro(l2)
    b1.mostrar_livros()
    print()

    b1.adicionar_livro(l3)
    b1.mostrar_livros()
    print()