class Livro:
    # Construtor para inicializar os atributos
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    # Método para mostrar informações do livro
    def mostrar_info(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.ano_publicacao}")


class Biblioteca:
    # Construtor para inicializar a biblioteca com uma capacidade definida
    def __init__(self, capacidade):
        self.livros = []  # Lista para armazenar os livros
        self.capacidade = capacidade

    # Método para adicionar um livro à biblioteca
    def adicionar_livro(self, livro):
        if len(self.livros) < self.capacidade:
            self.livros.append(livro)
            print("Livro adicionado com sucesso!")
        else:
            print("Biblioteca cheia. Não é possível adicionar mais livros.")

    # Método para mostrar todos os livros na biblioteca
    def mostrar_livros(self):
        print("Livros na Biblioteca:")
        for livro in self.livros:
            livro.mostrar_info()
            print()


# Testando a classe Biblioteca
biblioteca = Biblioteca(3)
biblioteca.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954))
biblioteca.adicionar_livro(Livro("1984", "George Orwell", 1949))
biblioteca.mostrar_livros()
