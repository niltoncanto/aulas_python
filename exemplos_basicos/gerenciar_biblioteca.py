class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

class Usuario:
    def __init__(self, nome, cpf, data_associacao):
        self.nome = nome
        self.cpf = cpf
        self.data_associacao = data_associacao

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, data_devolucao=None):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.livro.disponivel = False

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = []

    def cadastrar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.livros[isbn] = livro

    def cadastrar_usuario(self, nome, cpf, data_associacao):
        usuario = Usuario(nome, cpf, data_associacao)
        self.usuarios[cpf] = usuario

    def realizar_emprestimo(self, cpf_usuario, isbn_livro, data_emprestimo):
        if isbn_livro in self.livros and cpf_usuario in self.usuarios:
            livro = self.livros[isbn_livro]
            usuario = self.usuarios[cpf_usuario]
            if livro.disponivel:
                emprestimo = Emprestimo(usuario, livro, data_emprestimo)
                self.emprestimos.append(emprestimo)
                print(f"Empréstimo do livro '{livro.titulo}' para {usuario.nome} realizado com sucesso.")
            else:
                print("Livro não está disponível para empréstimo.")
        else:
            print("ISBN do livro ou CPF do usuário não encontrado.")

    def registrar_devolucao(self, isbn_livro):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.isbn == isbn_livro and not emprestimo.data_devolucao:
                emprestimo.data_devolucao = "Data atual"  # Simula a data atual de devolução
                emprestimo.livro.disponivel = True
                print(f"Devolução do livro '{emprestimo.livro.titulo}' registrada com sucesso.")
                return
        print("Empréstimo não encontrado ou livro já foi devolvido.")

    def exibir_menu(self):
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Usuário")
        print("3 - Realizar Empréstimo")
        print("4 - Registrar Devolução")
        print("5 - Visualizar Empréstimos")
        # Aqui viriam as implementações para interação com o usuário


if __name__=="__main__":
    biblioteca = Biblioteca()
    biblioteca.exibir_menu()