class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Membro:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

class RegistroEmprestimos:
    def __init__(self, membro):
        self.membro = membro
        self.emprestimos = []

    def adicionar_emprestimo(self, livro, data_emprestimo, data_devolucao):
        emprestimo = Emprestimo(livro, data_emprestimo, data_devolucao)
        self.emprestimos.append(emprestimo)
    
    def listar_emprestimos(self):
        if not self.emprestimos:
            print(f"{self.membro.nome} não tem empréstimos registrados.")
            return
        print(f"Empréstimos de {self.membro.nome}:")
        for emprestimo in self.emprestimos:
            print(f"Livro: {emprestimo.livro.titulo}, Data de Empréstimo: {emprestimo.data_emprestimo}, Data de Devolução: {emprestimo.data_devolucao}")

    def devolver_livro(self, isbn):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.isbn == isbn:
                self.emprestimos.remove(emprestimo)
                print(f"Livro {emprestimo.livro.titulo} devolvido com sucesso!")
                return True
        print("Empréstimo não encontrado!")
        return False

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}
        self.registros_emprestimos = []

    def incluir_livro(self):
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        isbn = input("ISBN do livro: ")
        livro = Livro(titulo, autor, isbn)
        self.livros[isbn] = livro
        print("Livro cadastrado com sucesso!")

    def incluir_membro(self):
        nome = input("Nome do membro: ")
        cpf = input("CPF do membro: ")
        data_nascimento = input("Data de nascimento do membro: ")
        membro = Membro(nome, cpf, data_nascimento)
        self.membros[cpf] = membro
        print("Membro cadastrado com sucesso!")

    def registrar_emprestimo(self):
        cpf_membro = input("CPF do membro: ")
        isbn_livro = input("ISBN do livro: ")
        data_emprestimo = input("Data de empréstimo: ")
        data_devolucao = input("Data de devolução: ")

        if cpf_membro in self.membros and isbn_livro in self.livros:
            membro = self.membros[cpf_membro]
            livro = self.livros[isbn_livro]
            registro = next((r for r in self.registros_emprestimos if r.membro.cpf == cpf_membro), None)
            if not registro:
                registro = RegistroEmprestimos(membro)
                self.registros_emprestimos.append(registro)
            registro.adicionar_emprestimo(livro, data_emprestimo, data_devolucao)
            print("Empréstimo registrado com sucesso!")
        else:
            print("Membro ou livro não encontrado!")

    def ver_emprestimos(self):
        if not self.registros_emprestimos:
            print("Nenhum empréstimo registrado.")
            return
        for registro in self.registros_emprestimos:
            registro.listar_emprestimos()

    def registrar_devolucao(self):
        cpf_membro = input("CPF do membro: ")
        isbn_livro = input("ISBN do livro: ")

        if cpf_membro in self.membros:
            registro = next((r for r in self.registros_emprestimos if r.membro.cpf == cpf_membro), None)
            if registro:
                if registro.devolver_livro(isbn_livro):
                    if not registro.emprestimos:
                        self.registros_emprestimos.remove(registro)
                        print(f"Todos os livros devolvidos por {registro.membro.nome}. Registro de empréstimos removido.")
            else:
                print("Nenhum empréstimo encontrado para este membro.")
        else:
            print("Membro não encontrado!")

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Incluir Livro")
            print("2. Incluir Membro")
            print("3. Registrar Empréstimo")
            print("4. Registrar Devolução")
            print("5. Ver Empréstimos")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.incluir_livro()
            elif opcao == "2":
                self.incluir_membro()
            elif opcao == "3":
                self.registrar_emprestimo()
            elif opcao == "4":
                self.registrar_devolucao()
            elif opcao == "5":
                self.ver_emprestimos()
            elif opcao == "6":
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.exibir_menu()
