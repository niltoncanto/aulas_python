from abc import ABC, abstractmethod

# Classe Abstrata MaterialBiblioteca
class MaterialBiblioteca():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    @abstractmethod
    def get_informacoes(self):
        print('Método abstrato')

# Subclasse Livro
class Livro(MaterialBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, num_paginas):
        super().__init__(titulo, autor, ano_publicacao)
        self.num_paginas = num_paginas
    
    def get_informacoes(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}, Ano: {self.ano_publicacao}"

# Subclasse Revista
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, edicao):
        super().__init__(titulo, autor, ano_publicacao)
        self.edicao = edicao
    
    def get_informacoes(self):
        return f"Revista: {self.titulo}, Autor: {self.autor}, Edição: {self.edicao}, Ano: {self.ano_publicacao}"

# Subclasse eBook
class eBook(MaterialBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, tamanho_arquivo):
        super().__init__(titulo, autor, ano_publicacao)
        self.tamanho_arquivo = tamanho_arquivo
    
    def get_informacoes(self):
        return f"eBook: {self.titulo}, Autor: {self.autor}, Tamanho: {self.tamanho_arquivo}MB, Ano: {self.ano_publicacao}"

# Subclasse Audiolivro
class Audiolivro(MaterialBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao, duracao):
        super().__init__(titulo, autor, ano_publicacao)
        self.duracao = duracao
    
    def get_informacoes(self):
        return f"Audiolivro: {self.titulo}, \
                Autor: {self.autor}, \
                Duração: {self.duracao} \
                horas, Ano: {self.ano_publicacao}"

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.materiais = []
    
    def adicionar_material(self, material):
        self.materiais.append(material)
    
    def remover_material(self, material):
        self.materiais.remove(material)
    
    def exibir_informacoes(self):
        for material in self.materiais:
            print(material.get_informacoes())

# Exemplo de Uso
biblioteca = Biblioteca()

livro = Livro("Python para Iniciantes", "João Silva", 2021, 300)
revista = Revista("Tech Today", "Maria Souza", 2023, "Edição 45")
ebook = eBook("Machine Learning Avançado", "Pedro Almeida", 2020, 5)
audiolivro = Audiolivro("Histórias da Vida", "Carlos Santos", 2022, 8)

biblioteca.adicionar_material(livro)
biblioteca.adicionar_material(revista)
biblioteca.adicionar_material(ebook)
biblioteca.adicionar_material(audiolivro)

biblioteca.exibir_informacoes()

material_biblioteca = MaterialBiblioteca("Python para Iniciantes", "João Silva", 2020)
material_biblioteca.get_informacoes()  # Erro: TypeError



