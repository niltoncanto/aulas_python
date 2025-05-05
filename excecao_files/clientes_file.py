import pickle

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"

class PessoaFisica(Cliente):
    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.cpf = cpf

    def __str__(self):
        return f"{super().__str__()}, CPF: {self.cpf}"

class PessoaJuridica(Cliente):
    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.cnpj = cnpj

    def __str__(self):
        return f"{super().__str__()}, CNPJ: {self.cnpj}"

class GerenciadorDeClientes:
    def __init__(self, arquivo_pkl):
        self.arquivo_pkl = arquivo_pkl
        try:
            with open(self.arquivo_pkl, 'rb') as arquivo:
                self.clientes_pf, self.clientes_pj = pickle.load(arquivo)
        except FileNotFoundError:
            self.clientes_pf = []
            self.clientes_pj = []

    def adicionar_cliente_pf(self, nome, email, cpf):
        cliente = PessoaFisica(nome, email, cpf)
        self.clientes_pf.append(cliente)
        print(f"Pessoa Física {cliente.nome} adicionada com sucesso.")

    def adicionar_cliente_pj(self, nome, email, cnpj):
        cliente = PessoaJuridica(nome, email, cnpj)
        self.clientes_pj.append(cliente)
        print(f"Pessoa Jurídica {cliente.nome} adicionada com sucesso.")

    def listar_clientes(self):
        print("Clientes Pessoa Física:")
        for cliente in self.clientes_pf:
            print(cliente)

        print("\nClientes Pessoa Jurídica:")
        for cliente in self.clientes_pj:
            print(cliente)

    def buscar_cliente_pf(self, indice):
        if 0 <= indice < len(self.clientes_pf):
            print(self.clientes_pf[indice])
        else:
            print("Cliente Pessoa Física não encontrado.")

    def buscar_cliente_pj(self, indice):
        if 0 <= indice < len(self.clientes_pj):
            print(self.clientes_pj[indice])
        else:
            print("Cliente Pessoa Jurídica não encontrado.")

    def excluir_cliente_pf(self, indice):
        if 0 <= indice < len(self.clientes_pf):
            removido = self.clientes_pf.pop(indice)
            print(f"Pessoa Física {removido.nome} removida com sucesso.")
        else:
            print("Cliente Pessoa Física não encontrado.")

    def excluir_cliente_pj(self, indice):
        if 0 <= indice < len(self.clientes_pj):
            removido = self.clientes_pj.pop(indice)
            print(f"Pessoa Jurídica {removido.nome} removida com sucesso.")
        else:
            print("Cliente Pessoa Jurídica não encontrado.")

    def salvar_dados(self):
        with open(self.arquivo_pkl, 'wb') as arquivo:
            pickle.dump([self.clientes_pf, self.clientes_pj], arquivo)
        print("Dados salvos com sucesso.")

def exibir_menu():
    print("\nEscolha uma das opções:")
    print("1. Adicionar Cliente (Pessoa Física)")
    print("2. Adicionar Cliente (Pessoa Jurídica)")
    print("3. Listar Clientes")
    print("4. Buscar Cliente (Pessoa Física por ID)")
    print("5. Buscar Cliente (Pessoa Jurídica por ID)")
    print("6. Excluir Cliente (Pessoa Física por ID)")
    print("7. Excluir Cliente (Pessoa Jurídica por ID)")
    print("8. Sair e Salvar")

def main():
    gerenciador = GerenciadorDeClientes('clientes.pkl')

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            cpf = input("CPF do cliente: ")
            gerenciador.adicionar_cliente_pf(nome, email, cpf)

        elif opcao == '2':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            cnpj = input("CNPJ do cliente: ")
            gerenciador.adicionar_cliente_pj(nome, email, cnpj)

        elif opcao == '3':
            gerenciador.listar_clientes()

        elif opcao == '4':
            indice = int(input("Digite o ID do cliente Pessoa Física: "))
            gerenciador.buscar_cliente_pf(indice)

        elif opcao == '5':
            indice = int(input("Digite o ID do cliente Pessoa Jurídica: "))
            gerenciador.buscar_cliente_pj(indice)

        elif opcao == '6':
            indice = int(input("Digite o ID do cliente Pessoa Física para excluir: "))
            gerenciador.excluir_cliente_pf(indice)

        elif opcao == '7':
            indice = int(input("Digite o ID do cliente Pessoa Jurídica para excluir: "))
            gerenciador.excluir_cliente_pj(indice)

        elif opcao == '8':
            gerenciador.salvar_dados()
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
