# Enunciado:  Você foi encarregado de criar um sistema para gerenciar uma biblioteca. 
# O sistema deve ser capaz de adicionar livros, limitando a quantidade com base na capacidade fornecida, e mostrar todos os livros cadastrados. 
# Implemente o sistema usando duas classes: Livro e Biblioteca.

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
    def __init__(self,titulo,autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_info(self):
        return f"Título:{self.titulo}\n Autor: {self.autor}\n Ano: {self.ano_publicacao}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.capacidade = 3
    
    def adicionar_livro(self,livro):
        if len(self.livros)<self.capacidade:
            self.livros.append(livro)
            return f"Livro {livro.titulo} inserido com sucesso!"
        else:
            return f"Não é possível inserir o livro, capacidade esgotada."

    def mostrar_livros(self):
        for i in self.livros:
            print(i.mostrar_info())

biblioteca = Biblioteca()
livro1 = Livro("Steve Jobs","Isaacson","2015")
livro2 = Livro("Saramago","Memorial do convento","2000")
print(biblioteca.adicionar_livro(livro1))
print(biblioteca.adicionar_livro(livro2))
print(biblioteca.adicionar_livro(Livro("Pablo Neruda","Confesso que vivi","1990")))
biblioteca.mostrar_livros()






    
            

