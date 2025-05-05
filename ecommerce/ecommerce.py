import uuid

class Pessoa:
    """ Representa uma pessoa com atributos básicos. cpf, nome, email"""
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Cliente:
    """ Representa um cliente do e-commerce, associado a uma pessoa. """
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.id_cliente = str(uuid.uuid4())  # Gera um identificador único


class Produto:
    """ Representa um produto disponível para venda. """
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


class ItemPedido:
    """ Representa um item dentro de um pedido. Contém um produto e uma quantidade. """
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.preco * self.quantidade


class Pedido:
    """ Representa um pedido realizado por um cliente. Contém o cliente e uma lista de itens. """
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.estoque >= quantidade:
            produto.estoque -= quantidade  # Reduz o estoque do produto
            item = ItemPedido(produto, quantidade)
            self.itens.append(item)
            return "Item adicionado ao pedido."
        return "Estoque insuficiente."

    def calcular_total(self):
        return sum(item.calcular_total() for item in self.itens)


class Menu:
    """ Gerencia o e-commerce, permitindo o cadastro de clientes, produtos e pedidos. """
    def __init__(self):
        self.clientes = {}  # Dicionário {CPF: Cliente}
        self.produtos = {}  # Dicionário {Nome: Produto}
        self.pedidos = []   # Lista de pedidos

    def cadastrar_cliente(self):
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        email = input("E-mail do cliente: ")
        
        if cpf in self.clientes:
            return "Cliente já cadastrado."

        pessoa = Pessoa(nome, cpf, email)
        cliente = Cliente(pessoa)
        self.clientes[cpf] = cliente
        return "Cliente cadastrado com sucesso!"

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        estoque = int(input("Quantidade em estoque: "))

        if nome in self.produtos:
            return "Produto já cadastrado."

        produto = Produto(nome, preco, estoque)
        self.produtos[nome] = produto
        return "Produto cadastrado com sucesso!"

    def criar_pedido(self):
        cpf = input("CPF do cliente: ")
        if cpf not in self.clientes:
            return "Cliente não encontrado."

        pedido = Pedido(self.clientes[cpf])

        while True:
            nome_produto = input("Nome do produto (ou 'sair' para finalizar o pedido): ")
            if nome_produto.lower() == "sair":
                break
            if nome_produto not in self.produtos:
                print("Produto não encontrado.")
                continue
            
            quantidade = int(input("Quantidade: "))
            resultado = pedido.adicionar_item(self.produtos[nome_produto], quantidade)
            print(resultado)

        if pedido.itens:
            self.pedidos.append(pedido)
            return f"Pedido criado com sucesso! Total: R$ {pedido.calcular_total():.2f}"
        return "Nenhum item adicionado ao pedido."

    def listar_pedidos(self):
        if not self.pedidos:
            return "Nenhum pedido registrado."
        
        for i, pedido in enumerate(self.pedidos, 1):
            print(f"\nPedido {i}: Cliente: {pedido.cliente.pessoa.nome} - {pedido.cliente.id_cliente}")
            for item in pedido.itens:
                print(f"- {item.produto.nome} (x{item.quantidade}) - R$ {item.calcular_total():.2f}")
            print(f"Total do Pedido: R$ {pedido.calcular_total():.2f}")
        
        return ""

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Cadastrar Cliente")
            print("2. Cadastrar Produto")
            print("3. Criar Pedido")
            print("4. Listar Pedidos")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                print(self.cadastrar_cliente())
            elif opcao == "2":
                print(self.cadastrar_produto())
            elif opcao == "3":
                print(self.criar_pedido())
            elif opcao == "4":
                print(self.listar_pedidos())
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
